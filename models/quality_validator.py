from PIL import Image
import numpy as np

def run(img):
    w, h = img.size
    print(verify_dimentions(w,h))
    print(verify_size(w,h))
    
def verify_dimentions(w,h):
    expected_width = 400
    expected_height = 200

    if w >= expected_width and h >= expected_height:
        return True
    else:
        return False

def verify_size(w,h):
    return True if w*h>460000 else False


if __name__=='__main__':
    img = Image.open("./IMG_20230326_095637_509.jpg")
    run(img)