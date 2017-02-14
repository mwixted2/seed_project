from time import sleep
import RPi.GPIO as GPIO
import sys
import os
from subprocess import Popen
#python wrapper around the omx player
from omxplayer import OMXPlayer

#tell the GPIO which pins to use
#either BCM or Board
GPIO.setmode(GPIO.BCM)
#turn off warnings i.e. "gpio pins are already in use"
GPIO.setwarnings(False)

#make instances of the videos to play
movie1 = OMXPlayer("/home/pi/seed_project/video1.mov")
movie2 = OMXPlayer('home/pi/seed_project/video2.mov')

#initialize input pins
#these are the buttons
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)


#initialize the output pins
#these are the LEDs
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(5, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)


#tell the LEDs to start active low
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
#GPIO.output(4, GPIO.LOW)
#GPIO.output(5, GPIO.LOW)
#GPIO.output(27, GPIO.LOW)
#GPIO.output(13, GPIO.LOW)


last_state1 = 1
last_state2 = 1
#last_state3 = 1
#last_state4 = 1
#last_state5 = 1
#last_state6 = 1

input_state1= 1
input_state2= 1
quit_video = 1
player = 0

while True:
	#set variable names to input pins
        input_state1 = GPIO.input(18)
        input_state2 = GPIO.input(23)
        #input_state3 = GPIO.input(24)
        #input_state4 = GPIO.input(25)
        #input_state5 = GPIO.input(12)
        #input_state6 = GPIO.input(16)

        
        if(input_state1 != last_state1):
        	if(player and not input_state1):
        		os.system('killall omxplayer.bin')
        		omxc = Popen(['omxplayer', '-b', movie1])
        		player = 1
         
        	elif not input_state1:
        		omxc = Popen(['omxplayer', movie2])
        		player = 1
           
   
		elif(input_state2 != last_state2):
       		if(player and not input_state2):
       			os.system('killall omxplayer.bin')
       			omxc = Popen(['omxplayer', '-b', movie2])
       			player = 1
       		elif not input_state2:
       			omxc = Popen(['omxplayer', '-b', movie2])
       			player = 1
		

		elif(player and input_state1 and input_state2):
      		os.system('killall omxplayer.bin')
      		player = 0

      	last_state1 = input_state1
      	last_state2 = input_state2
       
                        

#sleep(0.2);
