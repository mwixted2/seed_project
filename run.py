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
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#initalize videos and give path to each one
movie1 = ("/media/pi/PI/Morgan_trial/collard.mov")
movie2 = ("/media/pi/PI/Morgan_trial/corn.mov")
movie3 = ("/media/pi/PI/Morgan_trial/cowpeas.mov")
movie4 = ("/media/pi/PI/Morgan_trial/grape.mov")
movie5 = ("/media/pi/PI/Morgan_trial/lettuce.mov")
movie6 = ("/media/pi/PI/Morgan_trial/mustard.mov")
movie7 = ("/media/pi/PI/Morgan_trial/okra.mov")
movie8 = ("/media/pi/PI/Morgan_trial/peanut.mov")
movie9 = ("/media/pi/PI/Morgan_trial/pepper.mov")
movie10 = ("/media/pi/PI/Morgan_trial/pumpkin.mov")
movie11 = ("/media/pi/PI/Morgan_trial/roselle.mov")
movie12 = ("/media/pi/PI/Morgan_trial/sunflower.mov")
movie13 = ("/media/pi/PI/Morgan_trial/sweet-potato.mov")
movie14 = ("/media/pi/PI/Morgan_trial/tomato.mov")
movie15 = ("/media/pi/PI/Morgan_trial/watermelon.mov")
movie16 = ("/home/pi/seed_project/video1.mov")

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
last_state11 = True
last_state12 = True
last_state13 = True
last_state14 = True
last_state15 = True

#save the input state of the button
input_state1 = False
input_state2 = False
input_state3 = False
input_state4 = False
input_state5 = False
input_state6 = False
input_state7 = False
input_state8 = False
input_state9 = False
input_state10 = False
input_state11 = False
input_state12 = False
input_state13 = False
input_state14 = False
input_state15 = False
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
    input_state11 = GPIO.input(24)
    input_state12 = GPIO.input(25)
    input_state13 = GPIO.input(12)
    input_state14 = GPIO.input(16)
    input_state15 = GPIO.input(20)
    #quit_video = GPIO.input(24)

    #if first reed swtich is 
    if input_state1 != last_state1:
        if (player and input_state1):
            #omxplayer video
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True
        #checks for the other case: not input_state1
        #plays video if button is last_state1
        elif input_state1:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie1])
            player = True

    #if second button is pressed
    if input_state2 != last_state2:
        if (player and input_state2):
            #have to kill the any previous instances of omxplayer
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie2])
            player = True
        elif input_state2:
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

    #if eleventh button is pressed
    if input_state11 != last_state11:
        if(player and not input_state11):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxlayer', '-b', movie11])
            player = True
        elif not input_state11:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie11])
            player = True

    #if 12 button is pressed
    if input_state12 != last_state12:
        if(player and not input_state12):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie12])
            player = True
        elif not input_state12:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie12])
            player = True

    #if 13 button is pressed
    if input_state13 != last_state13:
        if(player and not input_state13):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie13])
            player = True
        elif not input_state13:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie13])
            player = True

    #if 14 button is pressed
    if input_state14 != last_state14:
        if(player and not input_state14):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie14])
            player = True
        elif not input_state14:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie14])
            player = True

    #if 15 button is pressed
    if input_state15 != last_state15:
        if(player and not input_state15):
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie15])
            player = True
        elif not input_state15:
            os.system('killall omxplayer.bin')
            omxc = Popen(['omxplayer', '-b', movie15])
            player = True

    #if omxplayer is running and none of the buttons are pressed
    if (player and input_state1 and input_state2 and input_state3 and input_state4 and input_state5 and input_state6 and input_state7 and input_state8 and input_state9 and input_state10 and input_state11 and input_state12 and input_state13 and input_state14 and input_state15):
        #os.system('killall omxplayer.bin')
        player = False


   
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
    last_state11 = input_state11
    last_state12 = input_state12
    last_state13 = input_state13
    last_state14 = input_state14
    last_state15 = input_state15
