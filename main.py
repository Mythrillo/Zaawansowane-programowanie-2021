import os

import cv2
import pytesseract
import numpy


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_text_from_image(img_path: str) -> str:
    # img = cv2.imread(img_path)
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_converted = clean_image(img_path)
    return pytesseract.image_to_string(img_converted)


def clean_image(img_path: str) -> numpy.ndarray:
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_converted = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img_converted = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img_converted = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img_converted = cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # img_converted = cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    # img_converted = cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    return img_converted


if __name__ == "__main__":
    # Need a folder called images with the dataset
    for filename in os.listdir("images"):
        print(filename)
        print(read_text_from_image(rf"images\{filename}"))
        print("###")
