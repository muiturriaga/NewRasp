#!/usr/bin/python

import time
import os
import threading


class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    print("ALARM NOW!")
                    os.popen("Tomorrowlandafter2012.mp3")
                    return
            time.sleep(60)
        except:
            return
    def just_die(self):
        self.keep_running = False





print("Hello, ")

alarm_HH = 01
alarm_MM = 00

print("You want to wake up at: {}:{}".format(alarm_HH, alarm_MM))


alarm = Alarm(alarm_HH, alarm_MM)
alarm.start()

try:
    while True:
         text = str(input())
         if text == "stop":
            alarm.just_die()
            break
except:
    print("Yikes lets get out of here")
    alarm.just_die()