#1
from PIL import Image, ImageFilter
import os
a = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpeg"]
def apply_filter(path1, path2):
    img = Image.open(path1)
    imgf = img.filter(ImageFilter.SHARPEN)
    imgf.save(path2)
    img.close()
dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(dir, "папка для картинок")
os.makedirs(output_dir, exist_ok=True)
for picture in a:
    path1 = os.path.join(dir, picture)
    path2 = os.path.join(output_dir, "новая картинка|" + picture)
    apply_filter(path1, path2)
#3
import csv
cnt=0
with open('Книга1.csv', newline='', encoding='cp1251') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, k, price = row
        k = int(k)
        price = int(price)
        cnt += k * price
        print(product,"-",k," шт. за", price," руб.")

print("Итоговая сумма: ",cnt,"руб." )

#2
from PIL import Image, ImageFilter
import os
a = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpeg", "6.png"]
def apply_filter(path1, path2):
    img = Image.open(path1)
    imgf = img.transpose(Image.ROTATE_180)
    imgf.save(path2)
    img.close()
dir = os.path.dirname(os.path.abspath(__file__))
dir2 = os.path.join(dir, "новая папка")
os.makedirs(dir2, exist_ok=True)
for pic in a:
    path1 = os.path.join(dir, pic)
    if pic.endswith(".jpg") or pic.endswith(".png"):
        path2 = os.path.join(dir2, "новая картинка" + pic)
        apply_filter(path1, path2)
