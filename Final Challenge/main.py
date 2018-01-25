#PeriwinkleOpossum
#Final Project
#Last Edited: 5th Dec, 2017
#Cited: Class Notes

from __future__ import division
import neuro
import linear_algebra
import numpy as np

data = open('my_test_cases.csv')
data = data.read()
data = data.split('\n')
data.pop()

inputs = []
targets = []

#creates inputs and targets
for i in data:
	tokens = i.split(',')
	inputs.append([float(tokens[0]),float(tokens[1]),float(tokens[2])])
	targets.append([float(tokens[3])])

repeats = 1300

#converts user_input to floats and divides in by 255 to have in a range of 0-1.0


network=[]

network = neuro.setup_network(inputs)

neuro.train(network, inputs, targets, repeats)
ans = 'yes'
while ans=='yes':
	r = float(raw_input('Enter Red Value (0,255): '))/255
	g = float(raw_input('Enter Green Value (0,255): '))/255
	b = float(raw_input('Enter Blue Value (0,255): '))/255
	test_input = [r,g,b]

	pred = neuro.predict(network,test_input)
	print pred
	pred = round(pred, 2)

	print pred
	if (pred>=0 and pred<0.33):
		print 'Your Color is RED'
	elif (pred>=0.33 and pred<0.66):
		print 'Your Color is GREEN'
	elif (pred>=0.66 and pred<=1):
		print 'Your Color is BLUE'

	ans = raw_input("Do you want to continue (yes/no): ")