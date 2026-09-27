from PIL import Image
import numpy
im1 = Image.open("1.png")
im2 = Image.open("2.png")
im2 = im2.resize(im1.size)
a = numpy.array(im1)
b = numpy.array(im2)

print(a.shape)
sum = 0.6*a+0.5*b
sum = sum.astype(numpy.uint8)
Image.fromarray(sum).save("sum.png")
