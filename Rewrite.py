#
# Rewrite.py
# Created by Catherine Wu and Daphne Weinstein
# 
# Rewrite who/what/when/where/why questions 
#

import nltk

# rewrite the question to facilitate querying the Twitter database for the answer
def rewriteQuestion(line):
	
	#grammar = r"""
  	#NP: {<DT|PP\$>?<JJ|JJS>*<NN>}   # chunk determiner/possessive, adjectives and noun
    #  {<NNP|VBN|JJ>+}                # chunk sequences of proper nouns
	#"""

	# use the grammar to find noun phrases
	grammar = r"""
	  NP: {<DT\$>?<JJ|JJS>*<NN>*}   # chunk determiner/possessive, adjectives and noun
	      {<NNP|NNS|NN|NNPS>+}                # chunk sequences of proper nouns
	"""
	cp = nltk.RegexpParser(grammar)
	tokens = nltk.word_tokenize(line)
	tags = nltk.pos_tag(tokens)

	# rewrite the question with the first noun phrase
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
			if len(rewrite) < 3:
				firstnp == False
				rewrite = ""
	#print(npnum)
	# if there is only one noun phrase, rewrite the question into answer form and return the rewrite
	if npnum == 1:
		i = 1
		firstwd = nltk.word_tokenize(rewrite)
		if len(firstwd) > 0:
			#print(firstwd[0])
			while tokens[i] != firstwd[0]:
				rewrite = rewrite + " " + tokens[i]
				i = i + 1
			#print "rewrite"
			#print(rewrite)
			
			return rewrite
	#START SUSPECT CODE====================================================================
	#print(tokens[0])
	elif tokens[0].lower() == "is":
		#print tags[len(tokens) - 2][1]
		if tags[len(tokens) - 3][1] == "DT":
			rewrite =  "\"" + rewrite + " " + " is " + tokens[len(tokens) - 3] + " " + tokens[len(tokens) - 2] + "\"" + " OR " + "\"" + rewrite + " " + " isn't " + tokens[len(tokens) - 3] + " " + tokens[len(tokens) - 2] + "\""
		elif tags[len(tokens) - 4][1] == "DT":
			rewrite =  "\"" + rewrite + " " + " is " + tokens[len(tokens) - 4] + " "+ tokens[len(tokens) - 3] + " " + tokens[len(tokens) - 2] + "\"" + " OR " + "\"" + rewrite + " " + " isn't " + tokens[len(tokens) - 4] + " " + tokens[len(tokens) - 3] + " " + tokens[len(tokens) - 2] + "\""
		else:
			rewrite = "\"" + rewrite + " " + " is " + tokens[len(tokens) - 2] + "\"" + " OR " + "\"" + rewrite + " " + " isn't " + tokens[len(tokens) - 2] + "\""
		return rewrite
			#END SUSPECT CODE====================================================================

	# otherwise, return "none" so that the question can be handled with the back-off scheme
	else:
		#print "none"
		return "none"

	




