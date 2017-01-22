import Adafruit_BBIO.GPIO as GPIO
import time

PIR_PIN = "P9_42"

GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print "PIR module test (press Ctrl-C to exit)"
    time.sleep(2)
    print "Ready"

    while True:
        if GPIO.input(PIR_PIN):
            print "Motion detected"
        time.sleep(1)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

