from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re

def ocr(path_to_image):
    # load the example image and convert it to grayscale
    image = cv2.imread(path_to_image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", gray)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)

    code = (re.findall("([0-9]+[-].+)", text))[0].split("-")

    return code
