from flask import Flask, request, jsonify
import numpy as np
from base64 import b64decode
import re
from models import easy, tesseract
import cv2


app = Flask(__name__)


@app.route("/", methods=["POST"])
def upload():
    data = request.get_json()

    img_b64 = data.get("image")
    img = prepare_img(img_b64)

    input_name = data.get("name")
    input_id = data.get("id")

    result = easy.reader(img)

    value = evaluate(input_name, input_id, result)

    output = {"isOk": value, "result": result}

    return jsonify(output)


def evaluate(input_name, input_id, result):
    test1 = all(word in result for word in input_name)
    test2 = input_id in result
    validation = test1 or test2
    return validation


def prepare_img(img_b64):
    img = re.sub("^data:image/.+;base64,", "", img_b64)
    img = np.frombuffer(b64decode(img), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img


if __name__ == "__main__":
    app.run(debug=True, port=2809, host="0.0.0.0")
