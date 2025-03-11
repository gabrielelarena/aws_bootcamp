import pytesseract
from PIL import Image

image_path = '/Users/kalamon/Downloads/Lista-de- Material.png'  
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)

print("Texto extraído:")
print(extracted_text)
