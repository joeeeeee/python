import pytesseract
from PIL import Image
import time
import subprocess

# image = Image.open('./tess2.jpg')
# print(image)
# text = pytesseract.image_to_string(image)
# print(text)

def cleanFile(filePath, newFilePath):
    # 打开图片
    image = Image.open(filePath)
    # 对图片进行阈值过滤，并保存
    image = image.point(lambda x:0 if x < 143 else 255)
    image.save(newFilePath)
    subprocess.call(['tesseract', newFilePath, 'output'])
    file = open('output.txt','r')
    print(file.read())
    file.close()


cleanFile('tess2.jpg', 'tesser' + str(time.time())+ '.png')

