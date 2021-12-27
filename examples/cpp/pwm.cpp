/**
 * Example using PWM with RGB led with pigpio
 *
 * sudo apt-get install pigpio
 * make
 * sudo ./pwm
 */
#include <iostream>
#include <cmath>
#include <pigpio.h>

float value(int i)
{
	if((i % 360) < 240)
		return std::sin((i % 360) * 2 * 3.1415 / 480.0f);
	else
		return 0.0f;
}

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

	gpioSetMode(14,PI_OUTPUT);
	gpioSetMode(15,PI_OUTPUT);
	gpioSetMode(18,PI_OUTPUT);

	while(true)
	{
		for(int i = 0; i < 360; ++i)
		{
			gpioPWM(14, 255 * value(i));
			gpioPWM(15, 255 * value(i + 120 % 360));
			gpioPWM(18, 255 * value(i + 240 % 360));
			gpioSleep(PI_TIME_RELATIVE, 0, 10 * 1000);
		}
	}

	gpioTerminate();
	return 0;
}
