import string;
import random;

def addCard(filename, question, answer, note):
	filename = 'shonagenius.txt'
	fileptr = open(filename, 'a')
	fileptr.writelines([question, "\t", answer, "\t\t\t\t\t", note, "\t", "\n"])
	fileptr.close()
	return [question, answer, "", "", "", "", note] 

def parseline(line):
	wordlist = string.split(line, '\t')
	if (len(wordlist) == 1 and wordlist[0] == ""):
		return []
	else:
		return wordlist;

def readtxt(filename, cardlist):
	card = [];
	open(filename, "a").close() #touch file
	fileptr = open(filename)
	#line  = fileptr.read()
	for line in fileptr:
		card = parseline(line)
		print "card %s" % card
		if (len(card) > 0):
			cardlist.append(card)
	fileptr.close()
	return cardlist;

def getquestion(card):
	if (card == []):
		return ""
	return card[0];

def getanswer(card):
	if (card == []):
		return ""
	return card[1];

def gettype(card):
	if (card == []):
		return ""
	return card[2];

def getnotes(card):
	if (card == []):
		return ""
	return card[6];

def getrandomcard(cardlist):
	if (len(cardlist) > 0):
		return cardlist[random.randint(0,len(cardlist) - 1)]
	else:
		return []

def readcards():
	mycardlist = [];
	mycardlist = readtxt('shonagenius.txt', mycardlist);
	return mycardlist
