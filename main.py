from prepare_img import run as prepare_img
from evaluate import run as evaluate

from flask import Flask, request, jsonify
from models import easy, tesseract

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


if __name__ == "__main__":
    app.run(debug=True, port=2809, host="0.0.0.0")
