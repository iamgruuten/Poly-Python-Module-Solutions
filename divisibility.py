
def cross():
  
  cross = [
  O,X,X,X,X,X,X,O,
  X,O,X,X,X,X,O,X,
  X,X,O,X,X,O,X,X,
  X,X,X,O,O,X,X,X,
  X,X,X,O,O,X,X,X,
  X,X,O,X,X,O,X,X,
  X,O,X,X,X,X,O,X,
  O,X,X,X,X,X,X,O
  ]
  
  return cross

def tick():
  
  tick = [
  X,X,X,X,X,X,X,X,
  X,X,X,X,X,X,X,X,
  X,X,X,X,X,X,X,O,
  X,X,X,X,X,X,O,X,
  X,X,X,X,X,O,X,X,
  O,X,X,X,O,X,X,X,
  X,O,X,O,X,X,X,X,
  X,X,O,X,X,X,X,X
  ]
  
  return tick
  
from sense_hat import SenseHat

S = SenseHat()
S.clear()
X=[255,255,255]
O=[255,0,0]


num = int(input("Please key in an integer number: "))
if (num % 6) == 0 and (num % 5) == 0:
  print("{} is divisble by 5 and 6".format(num))
  O=[0,255,0]
  S.set_pixels(tick())
else:
  print("{} is not divisble by 5 and 6".format(num))
  O=[255,0,0]
  S.set_pixels(cross())

    
