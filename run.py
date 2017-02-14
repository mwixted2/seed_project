#import gpio 
import RPi.GPIO as GPIO
#os to kill omxplayer instance
import os
#sys to kill omxplayer instance
import sys
#to play video
from subprocess import Popen
#using BCM set of pins instead of BOARD
#don't know why but it works better than BOARD
GPIO.setmode(GPIO.BCM)

#initialize pins to be inputs
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#initalize videos and give path to each one
movie1 = ("/home/pi/seed_project/video1.mov")
movie2 = ("/home/pi/seed_project/video2.mov")
movie3 = ("/media/pi/RASPBERRY_4/video3.mov")
movie4 = ("/home/pi/seed_project/video1.mov")

#save the last state of the button
last_state1 = True
last_state2 = True
last_state3 = True
last_state4 = True

#save the input state of the button
input_state1 = True
input_state2 = True
input_state3 = True
input_state4 = True

#only for debugging purposes
#quit_video = True

#player variable to toggle between player states
player = False

while True:
    #Read states of inputs
    input_state1 = GPIO.input(4)
    input_state2 = GPIO.input(17)
    input_state3 = GPIO.input(27)
    input_state4 = GPIO.input(5)
    #quit_video = GPIO.input(24)

    #if first button is pressed
    if input_state1 != last_state1:
        if (player and not input_state1):
            #omxplayer video
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True
       # elif not input_state1:
            #os.system('killalll omxplayer.bin')
           # omxc = Popen(['omxplayer', '-b', movie1])
            #player = True

    #if second button is pressed
    if input_state2 != last_state2:
        if (player and not input_state2):
            #have to kill the any previous instances of omxplayer
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie2])
            player = True
        elif not input_state2:
            omxc = Popen(['omxplayer', '-b', movie2])
            player = True

    #if third button is pressed
    if input_state3 != last_state3:
        if(player and not input_state3):
            #have to kill any previous instances of omxplayer
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie3])
            player = True
        elif not input_state3:
            omxc = Popen(['omxplayer', '-b', movie3])
            player = True

    if input_state4 != last_state4:
        if(player and not input_state4):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie4])
            player = True
        elif not input_state4:
            omxc = Popen(['omxplayer', '-b', movie4])
            player = True

    #if omxplayer is running and none of the buttons are pressed
    if (player and input_state1 and input_state2 and input_state3 and input_state4):
        #os.system('killall omxplayer.bin')
        player = False

    #GPIO(24) to close omxplayer manually - used during debug
    #if quit_video == False:
        #os.system('killall omxplayer.bin')
        #player = False

    #Set last_input states
    last_state1 = input_state1
    last_state2 = input_state2
    last_state3 = input_state3
    last_state4 = input_state4
