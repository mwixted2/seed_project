from time import sleep
import RPi.GPIO as GPIO
import sys
import os
from subprocess import Popen


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


movie1 = ("/home/pi/seed_projct/video1.mov")

GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)



GPIO.setup(17, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(5, GPIO.OUT)
#GPIO.setup(27, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)


GPIO.output(17, GPIO.LOW)
#GPIO.output(22, GPIO.LOW)
#GPIO.output(4, GPIO.LOW)
#GPIO.output(5, GPIO.LOW)
#GPIO.output(27, GPIO.LOW)
#GPIO.output(13, GPIO.LOW)


#last_state1 = 1
#last_state2 = 1
#last_state3 = 1
#last_state4 = 1
#last_state5 = 1
#last_state6 = 1

while True:
        input_state1 = GPIO.input(18)
        #input_state2 = GPIO.input(23)
        #input_state3 = GPIO.input(24)
        #input_state4 = GPIO.input(25)
        #input_state5 = GPIO.input(12)
        #input_state6 = GPIO.input(16)

        if(input_state1 == True):
        	oxmc = Popen(['omxplayer', movie1])
                #if(last_state1 == 1):
                        #GPIO.output(17, False)
            #oxmc = Popen(['omxplayer', movie1])
                        #last_state1 = 0
               # else:
                        #GPIO.output(17, True)
                        #last_state1 = 1
        #if(input_state2 == True):
                #if(last_state2 == 1):
                       # GPIO.output(22, False)
                       # last_state2 = 0
               # else:
                        #GPIO.output(22, True)
                        #last_state2 = 1
       # if(input_state3 == True):
       #         if(last_state3 == 1):
       #                 GPIO.output(4, False)
       #                 last_state3 = 0
       #         else:
       #                 GPIO.output(4, True)
       #                 last_state3 = 1
       # if(input_state4 == True):
        #        if(last_state4 == 1):
        #                GPIO.output(5, False)
        #                last_state4 = 0
        #        else:
        #                GPIO.output(5, True)
        #                last_state4 = 1

       # if(input_state5 == True):
       #         if(last_state5 == 1):
        #                GPIO.output(27, False)
       #                 last_state5 = 0
       #         else:
       #                 GPIO.output(27, True)
       #                 last_state5 = 1
       # if(input_state6 == True):
       #         if(last_state6 == 1):
       #                 GPIO.output(13, False)
       #                last_state6 = 0
       #         else:
        #                GPIO.output(13, True)
       #                 last_state6 = 1

       
                        

#sleep(0.2);
