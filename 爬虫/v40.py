
import pytesseract

from PIL import Image

# 生成图片实例
image = Image.open(r"C:\Users\SCzha\Desktop\shuzi3.jpg")

# 调用pytesseract, 把图片转换成文字
# 返回结过就是转化后的结果
text = pytesseract.image_to_string(image, lang="chi_sim")
print(text)