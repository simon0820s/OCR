from flask import Flask,request,jsonify
import numpy as np
from base64 import b64decode
import re
from class_p import Prediction


app=Flask(__name__)

@app.route('/', methods=["POST"])
def upload():
    data=request.get_json()
    img_b64=data.get("image")
    img=prepare_img(img_b64)
    
    return text.to_jsonify()

def prepare_img(img_b64):
    img = re.sub('^data:image/.+;base64,', '', img_b64)
    img = np.frombuffer(b64decode(img), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array([img]).astype(float)/255
    
    return img    
if __name__ == '__main__':
    app.run(debug=True, port=2809, host='0.0.0.0')