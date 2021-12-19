import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)
IO.setup(21,IO.IN)
IO.setup(20,IO.IN)
IO.setup(16,IO.IN)
IO.setup(12,IO.IN)
IO.setup(7,IO.IN)
IO.setup(8,IO.IN)

IO.setup(14,IO.IN)
IO.setup(15,IO.IN)
IO.setup(18,IO.IN)

rgb = 0

while 1:
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

	IO.setup(14,IO.IN)
	IO.setup(15,IO.IN)
	IO.setup(18,IO.IN)

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
