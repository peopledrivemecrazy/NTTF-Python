import RPi.GPIO as GPIO #Set name
import time # for timing functions

# Setup
GPIO.setmode(GPIO.BCM) # Set what method we are going to use to manipulate GPIO: BCM or BOARD
GPIO.setup(17, GPIO.OUT) # Set BCM pin 17 as output

# Loop
while True:
	GPIO.output(17, True) #Set BCM 17 to High
	print "LED ON"
	time.sleep(1) #Delay for 1 second
	GPIO.output(17, False) #Set BCM 17 to Low
	print "LED OFF" 
        time.sleep(1) #Delay for 1 second
