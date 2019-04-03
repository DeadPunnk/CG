from graphics import *
import time

win = GraphWin('', 500, 500)

win.setCoords(-100, -100, 100, 100)

# xi = 20
# xf = 60
# yi = 30
# yf = 100

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

xi = 2
xf = 9
yi = 3
yf = 6


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
      pt = Point(x, y)
      pt.draw(win)
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
      pt = Point(x, y)
      pt.draw(win)
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
      pt = Point(x,y)
      pt.draw(win)
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
      win.plot(x, y, "blue")
      if p < 0:
          y = y - 1
          p = p + (2 * delta_x)
      else:
          y = y - 1
          x = x + 1
          p = p + ((2 * delta_y) + (2*delta_x))
      print(x, ' ', y, ' ', p)

time.sleep(5)