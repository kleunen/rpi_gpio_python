# Introduction
In this lesson you will learn to program using the Python programming language. You will do this on an small computer called the Raspberry PI. This computer does not have a graphical interface, but you will have to program by typing in commands. 

# Step 1: Login to the system
Enter the system by typing in the username and password:

````
raspberrypi login: pi
Password: raspberry
````

After login, you will see a prompt: 
````
pi@raspberry:~ $
````

# Step 2: Start python

Start python by typing the python command:
````
pi@raspberry:~ $ python
````

When python has started you will see the python prompt:
````
>>>
````

# Step 3: Print hello world

Type the following command at the python prompt to tell the python language to print 'Hello world':

````
>>> print("Hello World!")
````

# Step 4: Turn a light (LED) on

We can turn on and off a light (LED) on the board using python commands. But first we need to setup some things:
````
>>> import RPi.GPIO as IO
>>> IO.setmode(IO.BCM)
````

After we have done this, we can turn a LED on:
````
>>> IO.setup(21,IO.OUT)  
````

And off again:
````
>>> IO.setup(21,IO.IN)  
````

# Step 5: Control all LEDS

We can turn the other LEDs on/off as well:

LED2:
````
>>> IO.setup(20,IO.OUT)  
>>> IO.setup(20,IO.IN)  
````

LED3:
````
>>> IO.setup(16,IO.OUT)  
>>> IO.setup(16,IO.IN)  
````

LED4:
````
>>> IO.setup(12,IO.OUT)  
>>> IO.setup(12,IO.IN)  
````

LED5:
````
>>> IO.setup(7,IO.OUT)  
>>> IO.setup(7,IO.IN)  
````

LED6:
````
>>> IO.setup(8,IO.OUT)  
>>> IO.setup(8,IO.IN)  
````

