import cv2
import easyocr

def reader ():
    reader = easyocr.Reader(["es"], gpu=False)
    image = cv2.imread("tif.jpeg")
    result = reader.readtext(image, detail=0)
    print(result)
if __name__=='__main__':
    reader()

