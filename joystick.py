from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

sense.clear()
flag=True
while flag:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        print("up")      # Up arrow
      elif event.direction == "down":
        print("down")      # Down arrow
      elif event.direction == "left": 
        print("left")      # Left arrow
      elif event.direction == "right":
        print("right")      # Right arrow
      elif event.direction == "middle":
        print("middle")      # Enter key
        flag=False
      
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()
  
print('End')
