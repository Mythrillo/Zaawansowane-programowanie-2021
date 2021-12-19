import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_text_from_image(img_path: str) -> str:
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


if __name__ == "__main__":
    img_paths = [rf"data\test{i}.jpg" for i in range(6)]
    for img in img_paths:
        print(f"Text in {img}:")
        print(read_text_from_image(img))
