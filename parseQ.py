import nltk
from getTweets import returnTweetsIS

grammar = r"""
  NP: {<DT|PP\$>?<JJ|JJS>*<NN>*}   # chunk determiner/possessive, adjectives and noun
      {<NNP|VBN>+}                # chunk sequences of proper nouns
"""
cp = nltk.RegexpParser(grammar)

line = raw_input("Enter Question: ")

tokens = nltk.word_tokenize(line)
tags = nltk.pos_tag(tokens)
tree = cp.parse(tags)

print tree
	
rewrite = ""
query = ""
np = ""
firstnp = False
for subtree in tree.subtrees():
	#print subtree
	if subtree.label() == 'NP':
		print "found"
		np = ""
		for tag in subtree:
			np = np + " " + tag[0]
		query = query + ", " + np
			#rewrite = ""
query = query[2:]
adjAdv = ""
#i = 0
print line
for item in nltk.pos_tag(tokens):
	#i = i + 1
	#sentence = sentence + str(item[0]) + " " + str(item[1]) + " "
	#print item[0]
	if (str(item[1]) == "RB" or str(item[1]) == 'JJ' or str(item[1]) == 'JJR' or str(item[1]) == 'JJS'):
		print "found adjectives or adverbs: "
		print item[0]
		adjAdv = adjAdv + ", " + item[0]
	#print item[1]
	#print i

print "Query: " + query
print "Adj + Adv: " + adjAdv
query = query + adjAdv
print "Final Query: " + query
returnTweetsIS(query)

	
#select shorter responses
#order of adjectives


#words = line.split()
#if len(words) == 1:
#	if len(blob.noun_phrases) >= 1:
#		query = blob.noun_phrases[0]
#		query = query + words[1]
#		print query 