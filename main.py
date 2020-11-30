import pyautogui as pag
import os 
import sys
import time 
import datetime

class Zoom():
	 
    def __init__(self, mid, pwd):
        self.mid = mid
        self.pwd = pwd
    
    def join_meeting(self):
        join = pag.locateCenterOnScreen('join.png')
        pag.click(join)
        time.sleep(2)
        meeting_id_bar = pag.locateCenterOnScreen('meeting_id.png')
        pag.click(meeting_id_bar)
        pag.write(str(self.mid))
        time.sleep(1)
        join_button = pag.locateCenterOnScreen('join_button.png')
        time.sleep(1)
        pag.press('enter')
        pag.click(join_button)
        pwd_bar = pag.locateCenterOnScreen('pwd.png')
        time.sleep(10)
        pag.click(pwd_bar)
        time.sleep(1)
        pag.write(str(self.pwd))
        pag.press('enter')


while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    time_now = str(current_time)
    strip_time = time_now.split(':')
    print(strip_time)
    if (strip_time[0] == '02') and (strip_time[1] == '18'):
        zoom = Zoom('266 170 7900','8PU492') 
        #zoom.openzoom()
        #time.sleep(10)
        zoom.join_meeting()
        break 

