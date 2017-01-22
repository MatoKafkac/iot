import Adafruit_BBIO.GPIO as GPIO
import time

PIR_PIN = "P9_42"

def MOTION(PIR_PIN):
    print "Motion detected"

#MV3 - setting pull up/down doesn't work(?)
#GPIO.setup(PIR_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback = MOTION)

try:
    print "PIR module test (press Ctrl-C to exit)"
    time.sleep(2)
    print "Ready"

    while True:
        #if GPIO.event_detected(PIR_PIN):
        #    print "Motion detected"
        time.sleep(1)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

