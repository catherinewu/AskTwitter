#
# postprocess.py
# Created by Catherine Wu and Daphne Weinstein
#
# After a set of tweets are returned, this program post processes the results according
# to the question type in order to return the best answer
#

import sys
import nltk
import twitter

# tries to find a tweet where the rewritten query is the start of the tweet
def postprocessWhoWhereWhat(tweetlist, query):
	if not tweetlist:
		return False
	found = False
	#print "query in postprocessWHO"
	#print query
	for tweet in tweetlist:
		#print "possible tweet: "
		#print tweet.text.encode('utf-8')
		if tweet.text.encode('utf-8').lower().startswith(query):
			if found == False:
				found = True
				print tweet.user.screen_name + ' (' + tweet.created_at + ')'
	   			print tweet.text.encode('utf-8')
	   			print ''
	if found == False:
		found = True
		#print "not found so printing first result"
		print tweet.user.screen_name + ' (' + tweet.created_at + ')'
	   	print tweet.text.encode('utf-8')
	   	print ''
   	return found

# not used yet
def postprocessIS(tweetlist, rewrite):
	for tweet in tweetlist:
		print tweet.text.encode('utf-8')

# post process when, what, where questions with scoring 
def postprocess(qtype, tweetlist, query):

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

	# iterate through the tweets and score each one
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
		scorelist.append(score - (len(response)/140))
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






