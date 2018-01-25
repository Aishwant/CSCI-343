from urllib2 import urlopen
from bs4 import BeautifulSoup

doc = urlopen('http://cloford.com/resources/colours/500col.htm')
html_file = doc.read()

soup = BeautifulSoup(html_file,'html.parser')

data = []

data1 = soup.find("table",{'class': 'webcol'})

rows = data1.find_all('tr')

for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	data.append([str(ele) for ele in cols if ele])

csv_file = open('my_test_cases.csv','w')

data = data[1:len(data)]
val = '0'
a = 38
b = 44
for i in data:
	tokens = i[0].split(',')
	# print tokens
	if tokens[0] == 'lightpink 4':
		continue
	elif tokens[0] == 'lavenderblush 3':
		continue
	elif tokens[0] == 'pink 4':
		continue
	elif tokens[0] == 'lavenderblush 4':
		continue
	elif tokens[0] == 'violetred':
		b = 0
	elif b <= 42:
		b=b+1
		continue
	elif tokens[0] == 'lightskyblue 4':
		continue
	elif tokens[0] == 'cadetblue 4':
		continue
	elif tokens[0] == 'lightsteelblue':
		continue
	elif tokens[0] == 'lightsteelblue 1':
		continue
	elif tokens[0] == 'lightsteelblue 2':
		continue
	elif tokens[0] == 'lightsteelblue 3':
		continue
	elif tokens[0] == 'lightsteelblue 4':
		continue
	elif tokens[0] == 'lightslategray':
		continue
	elif tokens[0] == 'slategray':
		continue
	elif tokens[0] == 'slategray 3':
		continue
	elif tokens[0] == 'slategray 4':
		continue
	elif tokens[0] == 'lightblue 2':
		a=0
	elif a <= 37:
		a=a+1
		continue
	# elif tokens[0] == 'lightcyan 3':
	# 	continue
	# elif tokens[0] == 'lightcyan 4':
	# 	continue
	# elif tokens[0] == 'paleturquoise 4':
	# 	continue
	# elif tokens[0] == 'darkslategray':
	# 	continue
	elif tokens[0] == 'coldgrey':
		continue
	elif tokens[0] == 'honeydew 2':
		continue
	elif tokens[0] == 'honeydew 3':
		continue
	elif tokens[0] == 'honeydew 4':
		continue
	elif tokens[0] == 'ivory 1 (ivory)':
		exit()

	if tokens[0] == 'darkslateblue':
		val = '1'
	elif tokens[0] == 'turquoiseblue':
		val = '0.5'
	csv_file.write(str(float(i[3])/255)+","+str(float(i[4])/255)+","+str(float(i[5])/255)+","+val+'\n')

csv_file.close()