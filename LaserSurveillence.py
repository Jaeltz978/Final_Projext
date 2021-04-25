from gpiozero import LightSensor
from time import sleep
import requests # idea from https://thepihut.com/blogs/raspberry-pi-tutorials/using-ifttt-with-the-raspberry-pi
ldr = LightSensor(4)

while True:
    sleep(0.3) # link to found
    if ldr.value < 0.5:
        http://requests.post('https://maker.ifttt.com/trigger/Laser_trip/with/key/noB6nShqQRFuBOW_CcodJlSVBC7wUWNZQhUi60078lT')
