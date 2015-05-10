# usage: python postscan_entities.py questiontype answers.txt

import sys
import nltk
import twitter


def postprocess(qtype, tweetlist):

	def otherq(tag, score):
		if tag == 'NNP' or tag == 'NNPS':
			score = score + 1

	def whenq(tag, score):
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
		if tag[1] == 'LS':
			score = score + 1
	

	score = 0
	scorelist = []
	for tweet in tweetlist:
		response = tweet.text.encode('utf-8')
		t = response.decode('utf8')
		tokens = nltk.word_tokenize(t)
		tags = nltk.pos_tag(tokens)
		for tag in tags:
			if qtype.lower() == "when":
				whenq(tag, score)	
			else:
				otherq(tag[1], score)	
		scorelist.append(score)
		score = 0
	scorelist.append(0)

	#find the maximum score in the list, iterate through till you find that score and 
	#return the thing at ans[that index] 
	maxs = max(scorelist)

	

	s = 0
	printed = False
	for tweet in tweetlist:
		if scorelist[s] == maxs and printed == False:
			print tweet.user.screen_name + ' (' + tweet.created_at + ')'
   			print tweet.text.encode('utf-8')
   			print ''
			printed = True
		s = s + 1

	if printed:
		return True
	else:
		return False






