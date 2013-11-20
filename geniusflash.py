import string;
import random;

def addCard(filename, question, answer, note):
	filename = 'shonagenius.txt'
	fileptr = open(filename, 'a')
	fileptr.writelines(["\n", question, "\t", answer, "\t\t\t\t\t", note, "\t"])
	fileptr.close()
	return [question, answer, "", "", "", "", note] 

def parseline(line):
	wordlist = string.split(line, '\t')
	return wordlist;

def readtxt(filename, cardlist):
	card = [];
	fileptr = open(filename)
	#line  = fileptr.read()
	for line in fileptr:
		card = parseline(line)
		print "card %s" % card
		cardlist.append(card)
	fileptr.close()
	return cardlist;

def getquestion(card):
	return card[0];

def getanswer(card):
	return card[1];

def gettype(card):
	return card[2];

def getnotes(card):
	return card[6];

def getrandomcard(cardlist):
	return cardlist[random.randint(0,len(cardlist) - 1)]

def readcards():
	mycardlist = [];
	mycardlist = readtxt('shonagenius.txt', mycardlist);
	return mycardlist
