# Periwinkle Opossum
# Challenge 5
# Last edited date: 15th Nov, 2017
# Citation - Challenge 1 and class notes

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot

data = open('PeriwinkleOpossum_ch5.csv')
data = data.read()
data = data.split('\n')
data.pop()
x=[]
y=[]
for i in data:
	tokens = i.split(',')
	if np.float(tokens[2]) < 42:
		x.append(np.float(tokens[0]))
		y.append(np.float(tokens[1]))
		
degree = 3
model_params = np.polyfit( x, y, degree)
x_required = range(0,350)
y_predicted = np.polyval(model_params,x_required )
mplot.title('Transition Time VS Signal Amplitude')
mplot.xlabel('Transition Time')
mplot.ylabel('Signal Amplitude')
mplot.plot(x_required, y_predicted)
mplot.scatter(x,y)
mplot.show()