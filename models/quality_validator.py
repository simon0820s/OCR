from PIL import Image
import numpy as np
import cv2

def run(img):
    w, h, c = img.shape
    dimentions = verify_dimentions(w,h)
    size = verify_size(w,h)
    blur = is_not_blurry(img)
    
    img_is_ok = True if dimentions[0] & size[0] & blur[0] else False
    
    return {
        "Dimentions": {
            "Dimentions": [dimentions[1],dimentions[2]],
            "DimentionsIsOK?":dimentions[0]
        },
        "Size": {
            "Size": size[1],
            "SizeIsOK?": size[0]
        },
        "Blur": {
            "BlurScore": blur[1],
            "BlurIsOK?": blur[0]
        },
        "ImgIsOK?": img_is_ok
    }
    
def verify_dimentions(w,h):
    expected_width = 400
    expected_height = 200

    if w >= expected_width and h >= expected_height:
        return [True,w,h]
    else:
        return [False,w,h]

def verify_size(w,h):
    return [True,w*h] if w*h>460000 else [False,w*h]

def is_not_blurry(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_score = cv2.Laplacian(gray_img, cv2.CV_64F).var()
    
    return [True,blur_score] if blur_score > 100 else [False, blur_score]

if __name__=='__main__':
    img = cv2.imread("./IMG_20230326_095637_509.jpg")
    run(img)