# Example showing how to read out the buttons on the board
import RPi.GPIO as IO
import time

# Use BCM pin names
IO.setmode(IO.BCM)

# The pin names and state for each button
buttons = [5,6,19,13,4,17]
button_state = [0] * 8

# Enable each button as input and use pull-down
for i in range(0, 6):
	print('Setup switch ', i+1, ' pin ' , buttons[i])
	IO.setup(buttons[i], IO.IN, pull_up_down=IO.PUD_DOWN)

# The led pin names
leds = [21, 20, 16, 12, 7, 8]
led_state = 0

# Disable all leds
for led in leds:
	IO.setup(led, IO.IN)

while 1: 
	
	# Scan through the different buttons
	for i in range(0, len(buttons)):

		# Check if button is pressed
		if IO.input(buttons[i]): 

			# Check if press was already detected
			if button_state[i] == 0:

				# A button was pressed
				button_state[i] = 1
				print('Switch ', i+1, 'pressed')

				IO.setup(leds[led_state%6], IO.IN)
				led_state = i
				IO.setup(leds[led_state%6], IO.OUT)

		else:

			# Check if the button was released again
			if button_state[i] == 1:
				button_state[i] = 0
				print('Switch ', i+1, 'released')

				
	time.sleep(0.01)

