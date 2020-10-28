'''
 programmed by Drew Scholz
 10/28/2020
 
 Magnet contact sensor
 Make sure wire connections are secure for accurate readings
'''

import RPi.GPIO as GPIO
import time

MAGNET_PIN = 37 #  26
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #BCM
GPIO.setup(MAGNET_PIN, GPIO.IN, GPIO.PUD_UP) #pull_up_down=GPIO.PUD_UP

while True:
    #print(GPIO.input(MAGNET_PIN))
    if GPIO.input(MAGNET_PIN) == 0:
        print('open')
    else:
        print('close')
    time.sleep(1)
