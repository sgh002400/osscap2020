import datetime
import pygame
import time
import os
import math
from datetime import datetime
from time import sleep

pygame.mixer.init()

audio_volume = 0.5 #0~1사이의 실수
audio_interval = 1

#print('{0}'.format(sound.get_volume()))


while True:
    ahour = int(input("What hour would you like to wake up at?(24 hour time): "))
    if (ahour > 23 or ahour < 0):
        print("please  re-enter")
        continue
    break

while True:
    aminute = int(input ("What minute would you like to wake up at?: "))
    if (aminute > 60 or aminute < 0):
        print("pleaes re-enter")
        continue
    break

pmh = 12

if ahour >= pmh:
    ap = "PM"
else:
    ap = "AM"

atime = "You want to wake up at %s:%s %s" % (str(ahour), str(aminute), ap)

atimeo = "%s:%s %s" % (str(ahour), str(aminute), ap)

print(atime)

timesran = 0

def counttimesran():
    global timesran
    timesran = timesran + 1

while True:
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour
    str(minute)
    
    if hour >= 12:
        pa = "PM"
    else:
        pa = "AM"
        
    real_time = "The time is:%s:%s:%s %s" % (hour, minute, second, pa)
    alarm_time = "%s:%s %s" % (hour, minute, pa)

    if (atimeo == alarm_time):
        print("WAKE UP")
        while True:
            sound = pygame.mixer.Sound('alarm.wav')
            sound.set_volume(audio_volume)
            sound.play()
            time.sleep(3)

print("End")