TARGETS=led buttons pwm

all: $(TARGETS)

led: led.cpp
	g++ -Wall -pthread -o led led.cpp -lpigpio -lrt
buttons: buttons.cpp
	g++ -Wall -pthread -o buttons buttons.cpp -lpigpio -lrt
pwm: pwm.cpp
	g++ -Wall -pthread -o pwm pwm.cpp -lpigpio -lrt

clean:
	rm -rf $(TARGETS)

