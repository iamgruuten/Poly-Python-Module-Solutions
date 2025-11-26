from sense_hat import SenseHat
import math as m

S = SenseHat()
S.clear()

temp = S.get_temperature()
RH = S.get_humidity()

T = temp * (9/5) + 32
HI = -42.38 + 2.05 * T + 10.14 * RH - 0.225 * T * RH - 0.007 * m.sqrt(T) - 0.0548 * m.sqrt(RH) + 0.00123*m.sqrt(T)* RH + 0.00085 * T * m.sqrt(RH)- 0.000002*m.sqrt(T)*m.sqrt(RH)
print(HI)

green = [0,255,0]
red = [255,0,0]
orange = [255, 165, 0]
yellow = [255, 255, 0]

if HI < 90:
  S.show_message("{}".format(HI),back_colour=green)
elif HI > 125:
  S.show_message("{}".format(HI),back_colour=red)
elif HI > 103:
  S.show_message("{}".format(HI),back_colour=orange)
else:
  S.show_message("{}".format(HI),back_colour=yellow)
  
