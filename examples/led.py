# Example showing how to use the LEDs and RGB led
import RPi.GPIO as IO
import time

# Use BCM pin names
IO.setmode(IO.BCM)

# Setup pins for LEDs as disabled (input)
IO.setup(21,IO.IN)
IO.setup(20,IO.IN)
IO.setup(16,IO.IN)
IO.setup(12,IO.IN)
IO.setup(7,IO.IN)
IO.setup(8,IO.IN)

# Setup pins for RGB as disabled (input)
IO.setup(14,IO.IN)
IO.setup(15,IO.IN)
IO.setup(18,IO.IN)

rgb = 0

while 1:
	# Enable each led one by one
	IO.setup(21,IO.OUT)
	time.sleep(0.1)
	IO.setup(20,IO.OUT)
	time.sleep(0.1)
	IO.setup(16,IO.OUT)
	time.sleep(0.1)
	IO.setup(12,IO.OUT)
	time.sleep(0.1)
	IO.setup(7,IO.OUT)
	time.sleep(0.1)
	IO.setup(8,IO.OUT)
	time.sleep(0.1)

	# Disable each led one by one
	IO.setup(21,IO.IN)
	time.sleep(0.1)
	IO.setup(20,IO.IN)
	time.sleep(0.1)
	IO.setup(16,IO.IN)
	time.sleep(0.1)
	IO.setup(12,IO.IN)
	time.sleep(0.1)
	IO.setup(7,IO.IN)
	time.sleep(0.1)
	IO.setup(8,IO.IN)
	time.sleep(0.1)

	# Setup pins for RGB as disabled (input)
	IO.setup(14,IO.IN)
	IO.setup(15,IO.IN)
	IO.setup(18,IO.IN)

	# Enable one of the RGB leds
	if rgb == 0: 
		IO.setup(14,IO.OUT)
		IO.output(14, IO.LOW)
		rgb = 1
	elif rgb == 1: 
		IO.setup(15,IO.OUT)
		IO.output(15, IO.LOW)
		rgb = 2
	elif rgb == 2: 
		IO.setup(18,IO.OUT)
		IO.output(18, IO.LOW)
		rgb = 0
