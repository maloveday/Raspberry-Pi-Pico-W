import max7219
from picozero import pico_led
from time import sleep
from machine import Pin, SPI

pico_led.on()
sleep(1)
pico_led.off()

# Assign chip select (CS) pint (and start it high)
cs = Pin(17, Pin.OUT)

# Initialise SPI
spi = SPI(0, baudrate=1000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(19))

display = max7219.Matrix8x8(spi, cs, 1)

# Display the number 1 followed by the number 2
for c in "12":
    display.fill(0)
    display.text(c,0,0,1)
    display.show()
    sleep(0.5)

# Turn on top left pixel
display.fill(0)
display.pixel(0,0,1)
display.show()
sleep(0.1)

# Turn on top right pixel
display.pixel(7,0,1)
display.show()
sleep(0.1)

# Turn on bottom right pixel
display.pixel(7,7,1)
display.show()
sleep(0.1)

# Turn on bottom left pixel
display.pixel(0,7,1)
display.show()
sleep(0.1)

# Scroll character to the left
display.fill(0)
display.text('1',0,0,1)
display.show()
sleep(0.5)

for i in range(8):
    display.scroll(-1,0)
    display.show()
    sleep(0.2)

# Scroll character to the right
display.fill(0)
display.text('1',0,0,1)
display.show()
sleep(0.5)

for i in range(8):
    display.scroll(1,0)
    display.show()
    sleep(0.2)

# Scroll message to the left
msg = "Hello World!"
for i in range(len(msg)*8):
    display.fill(0)
    display.text(msg,i*-1,0,1)
    display.show()
    sleep(1)
