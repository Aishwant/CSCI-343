#PeriwinkleOpossum
#Last edited: 29th August, 2017
#Challenger number 0.5
#Citation
#Journals.sagepub.com. (2017). The Virginia Opossum in Psychological ResearchPsychological Reports - Fred H. Herring, Donald J. Mason, John H. Doolittle, David E. Starrett, 1966. [online] Available at: http://journals.sagepub.com/doi/abs/10.2466/pr0.1966.19.3.755 [Accessed 28 Aug. 2017].


import os

def clearScreen():
	os.system("clear")

def main():
	file = open("opossumData.csv")

	data = file.read()
	tokens = data.split(',')
	clearScreen();

	list1 = {"Animal":"Opossum"}
	list1.update({"Scientific Name":"Didelphimorphia"})
	
	for x,y in list1.items():
		print x,":",y

	for tok in tokens:
		token = tok.split()

	print "\nSome facts about Opossum \n-----------------------------"

	for tok in tokens:
		print "-", tok
		
main()