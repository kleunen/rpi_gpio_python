# The Ladder Game
# (inspired by https://projects.drogon.net/raspberry-pi/gpio-examples/ladder-game/)

# Copyright (c) 2012 Pimoroni Ltd

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import time
import RPi.GPIO as IO

# setup constants for use late
LED_ON		= IO.LOW							  # led "on" state
LED_OFF		= IO.HIGH							  # led "off" state

button = 5									   # microswitch pin
leds   = [ 21, 20, 16, 12, 7, 8 ]			   # list of the IO pins connected to LEDs in display order

# runs the game
def run_game(): 
	level = 1					# start of level 1
	start = time.time()			# reset the clock
	current = LED_OFF			# initially the current level LED is off
	max_level = len(leds)		# maximum game level

	print("Game starting...")

	while True: # loop forever to keep the game running

		if IO.input( button ) == True: # was the switch pressed?

			# are we already on the last level? if so, win!
			if level == max_level:				
				win()												# show win animation
				return
			else:
				# was button was pressed while LED was on?
				if current == IO.LOW:
					print("Level up!")
					level = level + 1								# go to next level!
					time.sleep(0.5)
				else:
					lose()
					return

		# time in seconds per flash based on current level
		# time ranges from 1 second to 0.22 seconds
		time_per_flash =  1.0  / ( level / 2.0 ) 

		# check if it's time to blink the current level LED
		if time.time() - start > time_per_flash:
			current = IO.LOW if current == LED_OFF else LED_OFF # toggle the current level LED value
			IO.output( leds[ level - 1 ], current )		 # update the LED
			start = time.time()									# reset the clock


# displays the winning animation
def win():
	print("We have a winner!")

	# turn off all the LEDs
	all_leds(IO.HIGH)

	# do "knight rider" effect
	for y in range( 0, 10 ):
		# first light up each LED in squence
		for gpio_idx in leds[ 1:: ]:
			IO.output( gpio_idx, IO.LOW )
			time.sleep( .05 )
			IO.output( gpio_idx, LED_OFF )

		# then do the same in reverse
		for gpio_idx in leds[ ::-1 ]:
			IO.output( gpio_idx, IO.LOW )
			time.sleep( .05 )
			IO.output( gpio_idx, LED_OFF )

	# turn off all the LEDs
	all_leds(IO.HIGH)

# displays the losing animation
def lose():
	print("Game Over!")

	# flash all LEDs on and off
	for x in range( 0, 25 ):
		all_leds(IO.HIGH)
		time.sleep( .04 )
			
		all_leds(IO.LOW)
		time.sleep( .04 )

	# turn off all the LEDs
	all_leds(IO.HIGH)

# turns on/off all the LEDs
def all_leds(value):
	# turn off all the LEDs
	for gpio_idx in leds:
		IO.output( gpio_idx, value)


# sets up the IO mode and pins

# allow us to refer to IO pins by assigned number (rather than by position)
IO.setmode( IO.BCM )

# setup the switch pin for input and to return "True" on a down pulse
IO.setup( button, IO.IN, pull_up_down=IO.PUD_DOWN )

# set all of the LED IO pins to output mode
for gpio_idx in leds:
	IO.setup( gpio_idx, IO.OUT )

# turn off all the LEDs
all_leds(IO.HIGH)

# disable RGB leds
IO.setup(14,IO.IN)
IO.setup(15,IO.IN)
IO.setup(18,IO.IN)

run_game()
