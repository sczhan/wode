
import pytesseract

from PIL import Image

image = Image.open(r"C:\Users\SCzha\Desktop\shuzi3.jpg")

text = pytesseract.image_to_string(image, lang="chi_sim")
print(text)