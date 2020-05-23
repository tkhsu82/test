from PIL import Image
import os

size = 100

img = Image.open("C:/Users/tkhsu/Desktop/art.jpg")

imgSmall = img.resize((size,size), resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save('result.jpg')
#os.startfile('result.jpg')
print (result.size)

width, height = result.size
pixelValue = list(result.getdata())

print (pixelValue)