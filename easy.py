import cv2
import easyocr

def reader (img):
    
    reader = easyocr.Reader(["es"], gpu=False)
    result = reader.readtext(img, detail=0)
    
    return result
