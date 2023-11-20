import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image

image = Image.new('RGB',(100,100))

def brezenham_alg(start_x, start_y, end_x, end_y):
    if(start_x < end_x):
        x = start_x
        y = start_y
        last_x = end_x
        last_y = end_y
    else:
        x = end_x
        y = end_y
        last_x = start_x
        last_y = start_y

    if(x==last_x):
        y = min(start_y, end_y)
        last_y = max(start_y, end_y)

    dx = last_x - x
    dy = last_y - y

    if dx == 0:
        while y <= last_y:
            y+=1
        return

    tan = dy/dx

    incrN  = -2*dx
    incrNE = 2*(dy-dx)
    incrE  = 2*dy
    incrSE = 2*(dy+dx)
    incrS  = 2*dx

    d,low_incre, high_incre = 0,0,0
    """
    dy>1 : N - NE (y)
    0<dy<1 : NE - E (x)
    0>dy>-1 : E - SE (x)
    dy<-1 : SE - S (y)
    """

    if tan >1:
        high_incre = incrN
        low_incre  = incrNE
        d = dy-2*dx

    elif tan >0:
        high_incre = incrNE
        low_incre  = incrE
        d = 2*dy-dx

    elif tan >-1:
        high_incre = incrE
        low_incre  = incrSE
        d = 2*dy+dx

    else:
        high_incre = incrSE
        low_incre  = incrS
        d = dy+2*dx

    while x != last_x or (y != last_y if (tan>1 or tan<-1) else False):
        if d<= 0 :
            d+= low_incre
            if(tan>1):
                x+= 1
                y+= 1
                image.putpixel((x,y),(0,0,255)) #синий
            elif(tan<-1):
                y-=1
                image.putpixel((x,y),(255,160,122)) #светло оранжевый
            else:
                y+= 0 if tan>0 else -1
                x+= 1
                image.putpixel((x,y),(255, 165, 0)) #оранжевый
        else :
            d+= high_incre
            if(tan>1):
                y+=1
                image.putpixel((x,y),(128, 0, 128)) #фиолетовый
            elif(tan<-1):
                y-=1
                x+=1
                image.putpixel((x,y),(255,255,255)) #белый
            else:
                y+= 1 if tan>0 else 0
                x+= 1
                image.putpixel((x,y),(255,255,0)) #желтый
    plt.imshow(image)


#from PIL import ImageColor
# using getrgb for yellow
#img1 = ImageColor.getrgb("white")
#print(img1)
'''
#фиолетово-синие линии
i = 10
for i in range(90):
  brezenham_alg(0,0,10,i)
  i += 10

#оранжево-желтый верхний треугольник
j = 15
for j in range(100):
  brezenham_alg(0,0,20,j)
  j += 5

#оранжево-желтый нижний треугольник
s = 5
for s in range(100):
  brezenham_alg(0,s,20,80)
  s += 5
'''
#фиолетово-синий
brezenham_alg(5,-50,30,40)
brezenham_alg(5,-45,30,40)
brezenham_alg(5,-40,30,40)
brezenham_alg(5,-35,30,40)
brezenham_alg(5,-30,30,40)
brezenham_alg(5,-25,30,40)
brezenham_alg(5,-20,30,40)
brezenham_alg(5,-15,30,40)
brezenham_alg(5,-10,30,40)
brezenham_alg(5,-5,30,40)
brezenham_alg(5,0,30,40)
brezenham_alg(5,5,30,40)

#оранжево-желтый
brezenham_alg(5,10,30,40)
brezenham_alg(5,15,30,40)
brezenham_alg(5,20,30,40)
brezenham_alg(5,25,30,40)
brezenham_alg(5,30,30,40)
brezenham_alg(5,45,30,40)
brezenham_alg(5,50,30,40)
brezenham_alg(5,55,30,40)
brezenham_alg(5,60,30,40)
brezenham_alg(6,65,30,40)

#светло-оранжевый и белый
brezenham_alg(5,70,30,40)
brezenham_alg(5,75,30,40)
brezenham_alg(5,80,30,40)
brezenham_alg(5,85,30,40)
brezenham_alg(5,90,30,40)
brezenham_alg(5,95,30,40)
brezenham_alg(5,100,30,40)
