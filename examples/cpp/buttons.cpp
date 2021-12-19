/**
 * Example using LED with pigpio
 *
 * sudo apt-get install pigpio
 * make
 * sudo ./led
 */
#include <iostream>
#include <vector>
#include <pigpio.h>

int main()
{
	if(gpioInitialise() == 0)
		return -1;

	std::vector<unsigned int> leds = { 21, 20, 16, 12, 7, 8 };
	unsigned int led_state = 0;
	for(auto const i: leds)
		gpioSetMode(i,PI_INPUT);

	std::vector<unsigned int> buttons = {5, 6, 19, 13, 4, 17};
	std::vector<unsigned int> button_state = {0, 0, 0, 0, 0, 0};
	for(auto const i: buttons)
		gpioSetMode(i,PI_INPUT);

	gpioSetMode(14,PI_INPUT);
	gpioSetMode(15,PI_INPUT);
	gpioSetMode(18,PI_INPUT);

	while(true)
	{
		for(size_t i = 0; i < buttons.size(); ++i)
		{
			if(gpioRead(buttons[i])) {
				if(button_state[i] == 0) {
					button_state[i] = 1;
					std::cout << "Switch "  << i+1 << " pressed" << std::endl;

					gpioSetMode(leds[led_state],PI_INPUT);
					led_state = i;
					gpioSetMode(leds[led_state],PI_OUTPUT);
				}
			} else {
				if(button_state[i] == 1) {
					button_state[i] = 0;
					std::cout << "Switch "  << i+1 << " released" << std::endl;
				}
			}
		}

		gpioSleep(PI_TIME_RELATIVE, 0, 10 * 1000);
	}

	gpioTerminate();
	return 0;
}
