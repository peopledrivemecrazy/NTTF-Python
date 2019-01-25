import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

relay_condition = sys.argv[1] #Capture use input
print relay_condition
if relay_condition == "1":
	print "Relay On"
	GPIO.output(17, True)
if relay_condition == "0":
        print "Relay Off"
        GPIO.output(17, False)


