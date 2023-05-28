import pytesseract


def reader(img):
    text = pytesseract.image_to_string(img, lang='spa')
    return text
