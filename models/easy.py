import easyocr


# Function using easyOCR OCR input: img output: text of Optical Character Recognition
def reader(img):
    reader = easyocr.Reader(["es"], gpu=False) # Load reader set lang and set gpu boolean value
    result = reader.readtext(img, detail=0) # Get text from Optical Character Recognition and set detail=0 to receive only the detected string 

    return result
