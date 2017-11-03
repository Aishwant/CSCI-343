######################################################
#Owner: Aishwant Ghimire
#PeriwinkleOpossum
#Challenge4
#Last Edited: 1st November, 2017
#Cited: Class notes and some help of the Professor
######################################################
from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import math
us_outline = file('us_outline.csv')
us_outline = us_outline.read()
us_outline = us_outline.split('\n')
data = file('data.csv')
data = data.read()
data = data.split('\n')
data.pop()

x_us_outline = []
y_us_outline = []
x = []
y =[]
population = []
k = int(raw_input('Enter the k value: '))

for i in us_outline:
	tokens = i.split(',')
	x_us_outline.append(np.float32(tokens[0]))
	y_us_outline.append(np.float32(tokens[1]))

for i in data:
	tokens = i.split(',')
	x.append(np.float32(tokens[0]))
	y.append(np.float32(tokens[1]))
	population.append(np.float32(tokens[2]))

def dist(a,b):
	return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))

distance=[]
x_required=[]
y_required=[]
pop_required=[]
for row in range(195):
	for col in range(121):
		for i in range(len(x)):
			distance.append([row,col,x[i],y[i],dist([x[i],y[i]],[row,col]),population[i]])
		distance = sorted(distance, key=lambda val:val[4])
		dist1= distance[0:k]
		_, _, _ , _ , dis ,pop = zip(*dist1)
		pop_required.append(np.mean(pop))
		x_required.append(row)
		y_required.append(col)
		distance=[]

mplot.plot(x_us_outline,y_us_outline,c='#000000')
mplot.scatter(x_required,y_required,marker='s',c=pop_required, cmap="viridis")
mplot.show()