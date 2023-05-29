from base64 import b64decode
import numpy as np
import cv2
import re


# Function input: imgb64 output: binary img with modifications
def run(img_b64):
    img = re.sub("^data:image/.+;base64,", "", img_b64)  # delete prefix
    img = np.frombuffer(b64decode(img), dtype=np.uint8)  # decode b64 tobinary
    img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)  # decode to cv2
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # to gray scale

    return img
