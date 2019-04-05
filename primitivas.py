from graphics import *
import time

win = GraphWin('', 500, 500)
win.setCoords(-200, -200, 200, 200)

def ponto(x, y):
   pt = Point(x, y)
   pt.setOutline(color_rgb(255, 51, 153))
   pt.draw(win)

def circulo(x, y):
   # print(x, y)
   ponto(x, y)
   # print(y, x)
   ponto(y, x)
   # print(y, -x)
   ponto(y, -x)
   # print(-x, y)
   ponto(-x, y)
   # print(-x, -y)
   ponto(-x, -y)
   # print(-y, -x)
   ponto(-y, -x)
   # print(-y, x)
   ponto(-y, x)
   # print(x, -y)
   ponto(x, -y)
   # time.sleep(0.01)

x = 0
y = 150
p = 1 - 150

circulo(x, y)

while x < y:
   x = x + 1
   if p < 0:
       p = p + (2 * x) + 1
   else:
       y = y - 1
       p = p + (2 * x) + 1 - (2 * y)
   circulo(x, y)

def reta():
   pt = Point(0, 0)
   pt.draw(win)

   pt = Point(-10, 0)
   pt.draw(win)

   pt = Point(0, -10)
   pt.draw(win)

   pt = Point(0, 10)
   pt.draw(win)

   pt = Point(10, 0)
   pt.draw(win)

   xi = 20
   xf = 90
   yi = 30
   yf = 60

   x = xi
   y = yi

   delta_x = xf - xi
   print(delta_x)
   delta_y = yf - yi
   print(delta_y)

   m = delta_y / delta_x
   print(m)

   if m <= 1.0 and m > 0.0:
       p = (2 * delta_y) - delta_x
       print('1')
       while x <= xf:
           ponto(x, y)
           if p < 0:
               x = x + 1
               p = p + (2 * delta_y)
           else:
               x = x + 1
               y = y + 1
               p = p + (2 * delta_y) - (2 * delta_x)
           print(x, ' ', y, ' ', p)

   elif m < 0 and m > -1:
       p = (2 * delta_y) + delta_x
       print('2')
       while x != xf and y != yf:
           ponto(x, y)
           if p < 0:
               x = x + 1
               y = y - 1
               p = p + ((2 * delta_y) + (2 * delta_x))
           else:
               x = x + 1
               p = p + (2 * delta_y)
           print(x, ' ', y, ' ', p)
   elif m >= 1:
       p = delta_y - (2 * delta_x)
       print('3')
       while x != xf and y != yf:
           ponto(x, y)
           if p < 0:
               x = x + 1
               y = y + 1
               p = p + (2 * delta_y) - (2 * delta_x)
           else:
               y = y + 1
               p = p - (2 * delta_x)
           print(x, ' ', y, ' ', p)
   elif m < -1:
       p = delta_y + (2 * delta_x)
       print('4')
       while x != xf and y != yf:
           ponto(x, y)
           if p < 0:
               y = y - 1
               p = p + (2 * delta_x)
           else:
               y = y - 1
               x = x + 1
               p = p + ((2 * delta_y) + (2 * delta_x))
           print(x, ' ', y, ' ', p)

reta()

time.sleep(5)
