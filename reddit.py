from __future__ import print_function
import praw
import serial
import time

r = praw.Reddit(user_agent='unreadMessageChecker')
r.login('username', 'password')
ser = serial.Serial(2)
while True:
	if len(list(r.get_unread(limit=None))) > 0:
		ser.write("1")
		print("1")
	else:
		ser.write("0")
		print("0")
	time.sleep(60)
