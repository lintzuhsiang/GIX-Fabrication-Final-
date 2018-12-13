import time
import board
import audioio
from analogio import AnalogIn,AnalogOut
from digitalio import DigitalInOut, Direction, Pull
import neopixel
#initialize all ten LEDs and their brightness
led = neopixel.NeoPixel(board.NEOPIXEL, 10)
led.brightness = 0.3
#set analog input/output, only used in first iteration
analog_in = AnalogIn(board.A2)
analog_out = AnalogOut(board.A0)

# enable the speaker to play audio file
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

audiofiles = ["Go.wav","Huskies.wav"]

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def play_file(filename):
    wave_file = open(filename,'rb')
    with audioio.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                pass

blue = (0,0,255)
red = (255,0,0)
purple = (148,0,211)

while True:
    time.sleep(0.1)
    if (get_voltage(analog_in)) < 1.5:    # get low input, not connected
        led.fill(red)                     #another arm: led.fill(blue)
    
    else:                                 #get high input, connected
        led.fill(purple)
        play_file(audiofiles[0])          #another arm: play_file(audiofiles[1])
        
