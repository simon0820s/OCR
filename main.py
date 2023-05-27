from flask import Flask,request,jsonify
import numpy as np
from base64 import b64decode
import re
from easy import reader
import cv2


app=Flask(__name__)

@app.route('/', methods=["POST"])
def upload():
    data=request.get_json()
    img_b64=data.get("image")
    img=prepare_img(img_b64)
    
    result = reader(img)
    print(result)
    
    return result
    
def prepare_img(img_b64):
    img = re.sub('^data:image/.+;base64,', '', img_b64)
    img = np.frombuffer(b64decode(img), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
    
    return img  
  
if __name__ == '__main__':
    app.run(debug=True, port=2809, host='0.0.0.0')