from machine import ADC, Pin, PWM
from time import sleep_ms
from dht import DHT11

sensor=ADC(27)
bomba = machine.Pin(17, machine.Pin.OUT)

pin = Pin(26, Pin.IN, Pin.PULL_UP)
dht11=DHT11(pin, None, dht11=True)
ventilador = machine.Pin(16, machine.Pin.OUT)
ventilador.value(0)

while True:
    lectura=sensor.read_u16()
    T, H = dht11.read()
    if lectura > 55000:
        bomba.value(1)
    else:
        bomba.value(0)
    if T < 26:
        ventilador.value(1)
    else:
        ventilador.value(0)
        
    print(lectura)
    print(T)
    print(H)
    sleep_ms(2000)
    
