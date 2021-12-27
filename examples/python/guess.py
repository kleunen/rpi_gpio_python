# Guessing game

import RPi.GPIO as IO
import random
import time

# setup constants for use late
LED_ON		= IO.LOW							  # led "on" state
LED_OFF		= IO.HIGH							  # led "off" state

buttons = [5, 6, 19, 13, 4, 17]
button_state = [0] * len(buttons)
leds   = [ 21, 20, 16, 12, 7, 8 ]            

# runs the game
def run_game(): 
    print("Game starting...")

    max_level = len(leds)       # maximum game level
    all_leds(LED_OFF)         # turn off all the LED
    level = 1                   # start of level 1

    secret_values = [random.randint(0, 3) for i in range(0, max_level)]

    start = time.time() # reset the clock
    current = LED_OFF

    # Interval for flashing current level
    time_per_flash = 0.5

    while True: # loop forever to keep the game running

        for i in range(0, 6):
            if IO.input(buttons[i]): 
                button_state[i] = 1
            else:
                if button_state[i] == 1:
                    button_state[i] = 0

                    if i == secret_values[level-1]:
                        if level < max_level:
                            print("Level up!")
                            IO.output( leds[ level - 1 ], LED_ON )       # update the LED
                            level = level + 1                            # go to next level!
                            current = LED_OFF
                        else:
                            win()                                        # show win animation
                            return

                    else:
                        lose()
                        level = 1
                        all_leds(LED_OFF)
                        current = LED_OFF


        # check if it's time to blink the current level LED
        if time.time() - start > time_per_flash:
            current = LED_ON if current == LED_OFF else LED_OFF # toggle the current level LED value
            IO.output( leds[ level - 1 ], current )      # update the LED
            start = time.time()                                 # reset the clock

        time.sleep(0.01)
        

# displays the winning animation
def win():
    print("We have a winner!")

    # turn off all the LEDs
    all_leds(LED_OFF)

    # do "knight rider" effect
    for y in range( 0, 10 ):
        # first light up each LED in squence
        for gpio_idx in leds[ 1:: ]:
            IO.output( gpio_idx, LED_ON )
            time.sleep( .05 )
            IO.output( gpio_idx, LED_OFF )

        # then do the same in reverse
        for gpio_idx in leds[ ::-1 ]:
            IO.output( gpio_idx, LED_ON )
            time.sleep( .05 )
            IO.output( gpio_idx, LED_OFF )

    # turn off all the LEDs
    all_leds(LED_OFF)


# displays the losing animation
def lose():
    print("Game Over!")

    # flash all LEDs on and off
    for x in range( 0, 25 ):
        all_leds(LED_OFF)
        time.sleep( .04 )
            
        all_leds(LED_ON)
        time.sleep( .04 )

    # turn off all the LEDs
    all_leds(LED_OFF)


# turns on/off all the LEDs
def all_leds(value):
    # turn off all the LEDs
    for gpio_idx in leds:
        IO.output( gpio_idx, value)

IO.setmode( IO.BCM )

# setup the switch pin for input and to return "True" on a down pulse
for i in range(0, len(buttons)):
    print("Setup switch ", i+1, " pin ", buttons[i])
    IO.setup(buttons[i], IO.IN, pull_up_down=IO.PUD_DOWN)

# set all of the LED IO pins to output mode
for gpio_idx in leds:
    IO.setup( gpio_idx, IO.OUT )

# disable RGB leds
IO.setup(14,IO.IN)
IO.setup(15,IO.IN)
IO.setup(18,IO.IN)

print ("Enter the 6-digit pincode (s1-s4) to win the game!")
while True:
    run_game()
