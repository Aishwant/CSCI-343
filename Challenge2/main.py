#PeriwinkleOpossum
#Challenge 2
#Last editied: Sept 18th, 2017
#Citation - Class notes

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import re

dct = {}

def fileReader(fileReceived):
	data = open(fileReceived,"r")
	data = data.read()
	data = re.sub(r'\W+',' ',data)
	data = data.lower()
	data = data.split()
	data.pop()
	return data

def addToDict(data):
	for key in data:
		try:
			dct[key] = dct[key]+1
		except:
			dct[key] = 1

def addToListY(listY):
	y=0
	for key,value in listY.items(): y = y + value				
	return y

userInput = input("Files To Choose From: \n Republicans: r08, r12, r16 \n Democratic: d08, d12, d16 \n \t You want to choose---> ")
#userInput = raw_input("Files To Choose From: \n Republicans: r08, r12, r16 \n Democratic: d08, d12, d16 \n \t You want to choose---> ")  --python 2.7
print (userInput)
dataR = fileReader(userInput+".txt")
addToDict(dataR)

lexicon = open("sent_lexicon.csv","r")
lexicon = lexicon.read()
lexicon = lexicon.split("\n")
lexicon.pop()

lex =[]
for word in lexicon: lex.append(word.split(","))

lexWord=[] 
lexScore = []

for token in lexicon:
	tokens = token.split(",")
	lexWord.append(tokens[0])
	lexScore.append(float(tokens[1]))

pos={}
weaklyPos={}
neg={}
weaklyNeg={}
neutral={}

dctlex={}
for i in range(len(lexWord)): dctlex[lexWord[i]] = lexScore[i]

for key, value in dct.items():
		for kLex,vLex in dctlex.items():
			if(key==kLex):
			 	if(vLex > 0.6 and vLex <= 1.0):
			 		pos[key]=value
			 	elif(vLex > 0.2 and vLex <= 0.6):
			 		weaklyPos[key]=value
			 	elif(vLex == 0):
			 		neutral[key]=value
			 	elif(vLex >= -0.6 and vLex < -0.2):
			 		weaklyNeg[key]=value
			 	elif(vLex >= -1.0 and vLex < -0.6):
			 		neg[key]=value

x=[1,2,3,4,5]
y=[]

y.append(addToListY(neg)/len(dct)*100)
y.append(addToListY(weaklyNeg)/len(dct)*100)
y.append(addToListY(neutral)/len(dct)*100)
y.append(addToListY(weaklyPos)/len(dct)*100)
y.append(addToListY(pos)/len(dct)*100)

mplot.title("Sentiment Distribution from " + userInput.upper())
mplot.xlabel("Percentage of words")
mplot.ylabel("Sentiment")
mplot.xticks(x,["Negative","WeaklyNegative","Neutral","WeaklyPositive","Positive"])
mplot.bar(x,y)
mplot.show()