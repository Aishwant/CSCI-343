#PeriwinkleOpossum
#Last edited: 7th September, 2017
#Challenger number 1
#citation
#Class lectures

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot

data = open("PeriwinkleOpossum_ch1.csv")
data = data.read()
data = data.split("\n")
data.pop()

transTime =[]
signalAmp =[]
frequency =[]

for i in range(len(data)):
	tokens = data[i].split(",")
	if float(tokens[2]) < 23:
		transTime.append(float(tokens[0]))
		signalAmp.append(float(tokens[1]))
		frequency.append(float(tokens[2]))



dct = {}

for ele in transTime:
	try:
		dct[ele] = dct[ele]+1
	except:
		dct[ele] = 1



avgSignalAmp=[]
index = 0

for key, value in dct.items():
	sA = 0
	for v in range(value):
		sA=sA+signalAmp[index]
		index = index + 1 
	avgSignalAmp.append(sA/value)
	
	


x=[]
# x1 = sorted(list(set(transTime)))
for key,value in dct.items():
	x.append(key)

x = sorted(x)

mplot.xlabel("Milliseconds")
mplot.ylabel("Amplitude")
mplot.title("Amplitude VS. Time")
mplot.scatter(transTime,signalAmp)
mplot.plot(x, avgSignalAmp,'r')

mplot.show()
