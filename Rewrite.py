#
# Rewrite.py
# Created by Catherine Wu and Daphne Weinstein
# 
# Rewrite who/what/when/where/why questions 
#

import nltk

def rewriteQuestion(line):
	
	#grammar = r"""
  	#NP: {<DT|PP\$>?<JJ|JJS>*<NN>}   # chunk determiner/possessive, adjectives and noun
    #  {<NNP|VBN|JJ>+}                # chunk sequences of proper nouns
	#"""

	grammar = r"""
	  NP: {<PP\$>?<JJ|JJS>*<NN>*}   # chunk determiner/possessive, adjectives and noun
	      {<NNP|NNS|NN|NNPS|VBN>+}                # chunk sequences of proper nouns
	"""
	cp = nltk.RegexpParser(grammar)

	tokens = nltk.word_tokenize(line)
	tags = nltk.pos_tag(tokens)

	#REMOVE PRINT BELOW
	#print tags

	rewrite = ""
	tree = cp.parse(tags)
	#print(tree)
	firstnp = False
	npnum = 0
	for subtree in tree.subtrees():
		if subtree.label() == 'NP': 
			npnum = npnum + 1
			if firstnp == False:
				firstnp = True
				for tag in subtree:
					rewrite = rewrite + " " + tag[0]

	#print "npnum 2: "
	#print npnum

	if npnum == 1:
		print "hi"
		i = 1
		firstwd = nltk.word_tokenize(rewrite)
		if len(firstwd) > 0:
			#print(firstwd[0])
			while tokens[i] != firstwd[0]:
				rewrite = rewrite + " " + tokens[i]
				i = i + 1
			print "rewrite"
			print(rewrite)
			return rewrite
	#else push to is-question paradigm

	else:
		#print "none"
		return "none"




