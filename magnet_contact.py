'''
 programmed by Drew Scholz
 10/28/2020

 Magnet contact sensor
 Make sure wire connections are secure for accurate readings
'''

import RPi.GPIO as GPIO
import requests
import time
import json

instance_settings = json.loads(open("/home/pi/instance_settings.json", 'rb').read())
url = instance_settings.get('url', 'http://0.0.0.0:8000')

MAGNET_PIN = 37
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MAGNET_PIN, GPIO.IN, GPIO.PUD_UP)

open_count = 0
close_count = 0
state = None


def make_post(door_status):
    print(f"Making API call with door status {door_status}")
    params = dict(status=door_status)
    endpoint = url + '/api/door_magnet'
    headers = {'content-type': 'application/json'}
    try:
        response = requests.post(endpoint, headers=headers, verify=False, params=params)
    except requests.exceptions.ConnectionError as e:
        print("connection not open")
        pass

def stay_alive():
    '''
        Send the states so the FE knows you are active
    '''
    make_post(state)


'''
  Check magnet once per second.
  Make API call if the state of the door has changed after 3 consecutive seconds of the door state remaining the same
'''
print("\nStarting magnet sensor...\n")

lap = 0
while True:
    lap += 1
    if GPIO.input(MAGNET_PIN) == 0:
        #print('close')
        close_count += 1
        open_count = 0
        if close_count >= 3:
            if state != 'close':
                make_post('close')
            close_count = 0
            state = 'close'
    else:
        #print('open')
        open_count += 1
        close_count = 0
        if open_count >= 3:
            if state != 'open':
                make_post('open')
            open_count = 0
            state = 'open'

    time.sleep(1)
    if lap % 3600 == 0: # once per hour
        stay_alive()
        lap = 0
