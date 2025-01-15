from PIL import Image
import pytesseract
import sys

image_path = sys.argv[1]
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)

print(extracted_text)
