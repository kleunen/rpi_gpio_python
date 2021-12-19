import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)

buttons = [5,6,19,13,4,17]
button_state = [0] * 8

leds = [21, 20, 16, 12, 7, 8]
led_state = 0

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

				IO.setup(leds[led_state%6], IO.IN)
				led_state = i
				IO.setup(leds[led_state%6], IO.OUT)

		else:
			if button_state[i] == 1:
				new_led_state = 18 + random.randint(0, 6)
				button_state[i] = 0
				print('Switch ', i+1, 'released')

				
	time.sleep(0.01)

