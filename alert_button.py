import time
import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")
        response = requests.post("https://api.telegram.org/bot8854692912:AAGM9bI6eLRCvYIlFgTVRG7HHqgqLvr1Wxc/sendMessage", json={"chat_id": "6611321117", "text": "Someone pressed the alert button!"})

    elif GPIO.input(7) == GPIO.LOW:
    	button_pressed = False
    time.sleep(0.1)
