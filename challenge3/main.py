#PeriwinkleOpossum
#Challenge 3
#Last Edited: 5th October, 2017
#Citation: Notes and stackoverflow.com - Thank you StackOverFlow
from __future__ import division
from PIL import Image
import matplotlib.pyplot as mplot
import numpy as np
from path import path
def loopCondition():
	if(np.int32(user_input) >= 0 and np.int32(user_input) <= 255):
		return 1
	else:
		return 0

def standardDev(imageFiles,avg_img,N):
	s=0
	for i in imageFiles:
		s=s+(i - avg_img)**2
	return np.sqrt(s/N)		
#gets the path to the file
pathOfImages = path('unionconstruction')
imageFiles=[]
loopCond = 0
#checks condition
while loopCond==0:
	user_input = raw_input("Enter a a threshold value that ranges from 0 - 255: ")
	loopCond = loopCondition()
#converts string into integer
threshold = np.int32(user_input)
#appends the image converted matrix into the list
for i in pathOfImages.files():
	imageFile = Image.open(i)
	imageFiles.append(np.float32(imageFile))

avg_img = sum(imageFiles)/len(pathOfImages.files())
stdev_img = standardDev(imageFiles,avg_img,len(pathOfImages.files()))
avg_img=np.clip(avg_img,0,255)
stdev_img=np.clip(stdev_img,0,255)
#where the magic happens. Checks what value changed a lot.
for row in range(len(avg_img)):
	for col in range(len(avg_img[row])):
		if (stdev_img[row][col] > threshold).any():
			avg_img[row][col] = [255.0,0,0]
#with which nothing could be shown on the screen
avg_img = np.uint8(avg_img)
stdev_img = np.uint8(stdev_img)
mplot.imshow(avg_img)
mplot.show()