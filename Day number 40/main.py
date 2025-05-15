from PIL import Image


img = Image.open('/Users/milad-shah/Documents/GitHub/100DaysPython/Day number 40/milad.jpeg')


print(img.mode)
print(img.size)


pix = img.getpixel((100,100))

print(pix)

put_pix = img.putpixel((100 , 100), (255, 0, 0))

for i in range(10):
    for j in range(10):
        img.putpixel((100+i, 200+j), (i*10, i*10, j*10))


print(img.show())
