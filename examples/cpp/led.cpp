/**
 * Example using LED with pigpio
 *
 * sudo apt-get install pigpio
 * make
 * sudo ./led
 */
#include <iostream>
#include <pigpio.h>

int main()
{
	if(gpioInitialise() < 0) 
		return -1;

	gpioSetMode(21,PI_INPUT);
	gpioSetMode(20,PI_INPUT);
	gpioSetMode(16,PI_INPUT);
	gpioSetMode(12,PI_INPUT);
	gpioSetMode(7,PI_INPUT);
	gpioSetMode(8,PI_INPUT);

	gpioSetMode(14,PI_INPUT);
	gpioSetMode(15,PI_INPUT);
	gpioSetMode(18,PI_INPUT);

	unsigned int rgb = 0;

	while(true)
	{
		gpioSetMode(21,PI_OUTPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(20,PI_OUTPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(16,PI_OUTPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(12,PI_OUTPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(7,PI_OUTPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(8,PI_OUTPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);

		gpioSetMode(21,PI_INPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(20,PI_INPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(16,PI_INPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(12,PI_INPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(7,PI_INPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);
		gpioSetMode(8,PI_INPUT);
		gpioSleep(PI_TIME_RELATIVE, 0, 100 * 1000);

		gpioSetMode(14,PI_INPUT);
		gpioSetMode(15,PI_INPUT);
		gpioSetMode(18,PI_INPUT);

		if(rgb == 0)
			gpioSetMode(14,PI_OUTPUT);
		else if(rgb == 1)
			gpioSetMode(15,PI_OUTPUT);
		else
			gpioSetMode(18,PI_OUTPUT);
		rgb = (rgb + 1) % 3;
	}

	gpioTerminate();
	return 0;
}
