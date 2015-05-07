# usage: python postscan_entities.py questiontype answers.txt

import sys
import nltk

qtype = sys.argv[1]

answers = open(sys.argv[2], "r")
ans = answers.readlines()

def whowherewhatq(tag):
	if tag == NNP or tag == NNPS:
		score = score + 1

def whenq(tag):
	#months.txt .lower() 
	months = open("months.txt", "r")
	mo = months.readlines()
	for m in mo:
		if tag[0].lower() == m.lower():
			score = score + 2
	#eras.txt. lower()
	months = open("eras.txt", "r")
	era = months.readlines()
	for e in era:
		if tag[0].lower() == e.lower():
			score = score + 2
	#find a way to do years
	if tag[0].isdigit():
		score = score + 1
	#LS = list item marker, weighted less heavily than other types of markers
	if tag[1] == LS:
		score = score + 1


#else just select most recent 

score = 0
scorelist = []
for line in ans:
	tokens = nltk.word_tokenize(line)
	tags = nltk.pos_tag(tokens)
	for tag in tags:
		if qtype == "who"|"where"|"what":
			whoq(tag[1])
		if qtype == "when":
			whenq(tag)		
	scorelist.append(score)
	score = 0

answers.close()

#find the maximum score in the list, iterate through till you find that score and 
#return the thing at ans[that index] 
maxs = max(scores)

answers2 = open(sys.argv[2], "r")
ans2 = answers2.readlines()

s = 0
printed = False
for a in ans2:
	if scorelist[s] == maxs and printed == False:
		print(a)
		printed = True
	s = s + 1

answers2.close()






