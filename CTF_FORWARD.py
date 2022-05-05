#!/usr/bin/python3
from time import sleep
import RPi.GPIO as GPIO
#import time

SLEEP = 26 # 26 
DIR = 20  #Direction GPIO pin
STEP = 21 #step GPIO pin
CW = 1    #CW rotation
CCW = 0     #CCW rotation
SPR = 5000 #steps per reolution (360/step_angle=200  360/1.8=200)
a = 1.8 #Stepangle of Nema 17 HS4401
STAF= (a/360)*60*SPR #STepAngleFrequentie = (a°/360°)*60sec 


print(STAF ,SPR)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(SLEEP, GPIO.OUT) #uitgang 26 activeren
GPIO.output(SLEEP, GPIO.LOW) #uitgang 26 laag
GPIO.output(DIR, CCW)

step_count = SPR #SPR
delay = .005  # 1 seconde / SPR  0.0005

sleep(0.5)
GPIO.output(SLEEP, GPIO.HIGH)
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP,GPIO.LOW)
    sleep(delay)

GPIO.output(SLEEP, GPIO.LOW)
GPIO.cleanup()
