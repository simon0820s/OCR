from base64 import b64decode
import numpy as np
import cv2
import re

def run(img_b64):
    img = re.sub("^data:image/.+;base64,", "", img_b64)
    img = np.frombuffer(b64decode(img), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img