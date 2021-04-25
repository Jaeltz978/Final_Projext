from gpiozero import LightSensor
import time
import requests # idea from https://thepihut.com/blogs/raspberry-pi-tutorials/using-ifttt-with-the-raspberry-pi
ldr = LightSensor(4)

while True:
    time.sleep(0.3) # code from https://realpython.com/python-sleep/
    if ldr.value < 0.5:
        requests.post('https://maker.ifttt.com/trigger/Laser_trip/with/key/noB6nShqQRFuBOW_CcodJlSVBC7wUWNZQhUi60078lT')
