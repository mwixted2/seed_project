import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

movie1 = ("/home/pi/seed_project/video1.mov")
movie2 = ("/home/pi/seed_project/video2.mov")
movie3 = ("/media/pi/RASPBERRY_4/video3.mov")

last_state1 = True
last_state2 = True
last_state3 = True

input_state1 = True
input_state2 = True
input_state3 = True
quit_video = True

#player = False

while True:
    #Read states of inputs
    input_state1 = GPIO.input(4)
    input_state2 = GPIO.input(17)
    input_state3 = GPIO.input(27)
    #quit_video = GPIO.input(24)

    #If GPIO(17) is shorted to Ground
    if input_state1 != last_state1:
        if (player and not input_state1):
            omxc = Popen(['omxplayer', '-b', movie1])
            #player = True
        elif not input_state1:
            #os.system('killalll omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie1])
            #player = True

    #If GPIO(18) is shorted to Ground
    if input_state2 != last_state2:
        if (player and not input_state2):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie2])
            #player = True
        elif not input_state2:
            omxc = Popen(['omxplayer', '-b', movie2])
            #player = True

    if input_state3 != last_state3:
        if(player and not input_state3):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie3])
            #player = True
        elif not input_state3:
            omxc = Popen(['omxplayer', '-b', movie3])
            #player = True

    #If omxplayer is running and GIOP(17) and GPIO(18) are not shorted to Ground
    if (player and input_state1 and input_state2 and input_state3):
        #os.system('killall omxplayer.bin')
        #player = False

    #GPIO(24) to close omxplayer manually - used during debug
    if quit_video == False:
        #os.system('killall omxplayer.bin')
        player = False

    #Set last_input states
    last_state1 = input_state1
    last_state2 = input_state2
    last_state3 = input_state3
