import pytesseract

#Function using pytesseract OCR input: img output: text of Optical Character Recognition
def reader(img):
    text = pytesseract.image_to_string(img, lang='spa') #Load model an set lang
    return text
