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
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#initalize videos and give path to each one
movie1 = ("/home/pi/seed_project/video1.mov")
movie2 = ("/home/pi/seed_project/video2.mov")
movie3 = ("/media/pi/RASPBERRY_4/video3.mov")
movie4 = ("/home/pi/seed_project/video1.mov")
movie5 = ("/home/pi/seed_project/video2.mov")
movie6 = ("/media/pi/RASPBERRY_4/video3.mov")
movie7 = ("/home/pi/seed_project/video1.mov")
movie8 = ("/home/pi/seed_project/video2.mov")
movie9 = ("/media/pi/RASPBERRY_4/video3.mov")
movie10 = ("/home/pi/seed_project/video1.mov")

#save the last state of the button
last_state1 = True
last_state2 = True
last_state3 = True
last_state4 = True
last_state5 = True
last_state6 = True
last_state7 = True
last_state8 = True
last_state9 = True
last_state10 = True

#save the input state of the button
input_state1 = True
input_state2 = True
input_state3 = True
input_state4 = True
input_state5 = True
input_state6 = True
input_state7 = True
input_state8 = True
input_state9 = True
input_state10 = True
#only for debugging purposes
#quit_video = True

#player variable to toggle between player states
player = False

while True:
    #Read states of inputs
    input_state1 = GPIO.input(4)
    input_state2 = GPIO.input(17)
    input_state3 = GPIO.input(27)
    input_state4 = GPIO.input(22)
    input_state5 = GPIO.input(5)
    input_state6 = GPIO.input(6)
    input_state7 = GPIO.input(13)
    input_state8 = GPIO.input(26)
    input_state9 = GPIO.input(18)
    input_state10 = GPIO.input(23)
    #quit_video = GPIO.input(24)

    #if first button is pressed
    if input_state1 != last_state1:
        if (player and not input_state1):
            #omxplayer video
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True
        #checks for the other case: not input_state1
        #plays video if button is last_state1
        elif not input_state1:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True

    #if second button is pressed
    if input_state2 != last_state2:
        if (player and not input_state2):
            #have to kill the any previous instances of omxplayer
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie2])
            player = True
        elif not input_state2:
            #kill any previous instances of omxplayer
            os.system('killall omxplayer.bin')
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
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie3])
            player = True

    #if fourth button is pressed
    if input_state4 != last_state4:
        if(player and not input_state4):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie4])
            player = True
        elif not input_state4:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie4])
            player = True

    #if fifth button is pressed
    if input_state5 != last_state5:
        if(player and not input_state5):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie5])
            player = True
        elif not input_state5:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie5])
            player = True

    #if sixth button is pressed
    if input_state6 != last_state6:
        if(player and not input_state6):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie6])
            player = True
        elif not input_state6:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie6])
            player = True

    #if seventh button is pressed
    if input_state7 != last_state7:
        if(player and not input_state7):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie7])
            player = True
        elif not input_state7:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie7])
            player = True

    #if eighth button is pressed
    if input_state8 != last_state8:
        if(player and not input_state8):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie8])
            player = True
        elif not input_state8:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie8])
            player = True

    #if ninth button is pressed
    if input_state9 != last_state9:
        if(player and not input_state9):
            os.system('kilall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie9])
            player = True
        elif not input_state9:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie9])
            player = True

    #if tenth button is pressed
    if input_state10 != last_state10:
        if(player and not input_state10):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie10])
            player = True
        elif not input_state10:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie10])
            player = True


    #if omxplayer is running and none of the buttons are pressed
    if (player and input_state1 and input_state2 and input_state3 and input_state4 and input_state5 and input_state6 and input_state7 and input_state8 and input_state9 and input_state10):
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
    last_state5 = input_state5
    last_state6 = input_state6
    last_state7 = input_state7
    last_state8 = input_state8
    last_state9 = input_state9
    last_state10 = input_state10
