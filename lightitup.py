from sense_hat import SenseHat

S = SenseHat()
S.clear()
x=7
y=7
S.set_pixel(x,y,255,255,0)

while True:
  
  for event in S.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":y += 1
      elif event.direction == "down":y-=1
      elif event.direction == "left":x -=1
      elif event.direction == "right":x += 1
      if y > 7:
        y=0
      elif y == -1:
        y=7
    
      if x == 8:
        x=0
      elif x == -1:
        x=7
      S.clear()
      S.set_pixel(x,y,255,255,0)
    
