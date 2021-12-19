import RPi.GPIO as IO
import time
import random

IO.setmode(IO.BCM)

buttons = [5,6,19,13,4,17]
button_state = [0] * 8

leds = [21, 20, 16, 12, 7, 8]
led_state = 0
new_led_state = 0

for led in leds:
	IO.setup(led, IO.IN)
IO.setup(leds[led_state%6], IO.OUT)

for i in range(0, 6):
	print('Setup switch ', i+1, ' pin ' , buttons[i])
	IO.setup(buttons[i], IO.IN, pull_up_down=IO.PUD_DOWN)

while 1: 
	for i in range(0, 6):
		if IO.input(buttons[i]): 
			if button_state[i] == 0:
				button_state[i] = 1
				print('Switch ', i+1, 'pressed')
		else:
			if button_state[i] == 1:
				new_led_state = 18 + random.randint(0, 6)
				button_state[i] = 0
				print('Switch ', i+1, 'released')

				
	if new_led_state > 0:
		IO.setup(leds[led_state%6], IO.IN)

		led_state = (led_state + 1) % 6
		new_led_state = new_led_state - 1

		IO.setup(leds[led_state%6], IO.OUT)

		IO.setup(14,IO.IN)
		IO.setup(15,IO.IN)
		IO.setup(18,IO.IN)

		if led_state%3 == 0: 
			IO.setup(14,IO.OUT)
			IO.output(14, IO.LOW)
		elif led_state%3 == 1: 
			IO.setup(15,IO.OUT)
			IO.output(15, IO.LOW)
		elif led_state%3 == 2: 
			IO.setup(18,IO.OUT)
			IO.output(18, IO.LOW)

		if new_led_state > 3:
			time.sleep(0.1)
		elif new_led_state > 1:
			time.sleep(0.15)
		else:
			time.sleep(0.2)

					

	time.sleep(0.01)

