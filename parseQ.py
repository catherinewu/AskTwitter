import nltk
from getTweets import returnTweets

def findAnswer(line):
	found = False
	grammar = r"""
	  NP: {<PP\$>?<JJ|JJS>*<NN>*}   # chunk determiner/possessive, adjectives and noun
	      {<NNP|VBN>+}                # chunk sequences of proper nouns
	"""
	cp = nltk.RegexpParser(grammar)

	#line = raw_input("Enter Question: ")

	tokens = nltk.word_tokenize(line)
	tags = nltk.pos_tag(tokens)
	tree = cp.parse(tags)

	#print tree
		
	#rewrite = ""
	i = 0;
	query = ""
	query1 = ""
	query2 = ""
	np = ""
	firstnp = False
	for subtree in tree.subtrees():
		#print subtree
		if subtree.label() == 'NP':
			#print "found"
			i = i + 1
			np = ""
			for tag in subtree:
				np = np + " " + tag[0]
			query = query + " AND " + "\"" + np[1:] + "\""
			if i == 1:
				query1 = query1 + " AND " + "\"" + np[1:] + "\""
				query2 = query2 + " AND " + "\"" + np[1:] + "\""
			elif i == 2:
				query2 = query2 + " AND " + "\"" + np[1:] + "\""
				#rewrite = ""
	query = query[4:]
	query1 = query1[4:]
	query2 = query2[4:]

	#adjAdv = ""

	#for item in nltk.pos_tag(tokens):
	#	if (str(item[1]) == "RB" or str(item[1]) == 'JJ' or str(item[1]) == 'JJR' or str(item[1]) == 'JJS'):
	#		print "found adjectives or adverbs: "
	#		print item[0]
	#		adjAdv = adjAdv + " OR " + item[0]

	print "Query: " + query
	#print "Adj + Adv: " + adjAdv
	#query = query + adjAdv #+ " , not"
	#print "Final Query: " + query

	responses = returnTweets(query)
	if responses:
		found = True
		tweet = responses[0]
		print tweet.user.screen_name + ' (' + tweet.created_at + ')'
   		print tweet.text.encode('utf-8')
   		print ''

	if not found:
		responses = returnTweets(query2)
		if responses: 
			found = True
			tweet = responses[0]
			print tweet.user.screen_name + ' (' + tweet.created_at + ')'
   			print tweet.text.encode('utf-8')
   			print ''

   	if not found:
   		responses = returnTweets(query1)
		if responses: 
			found = True
			tweet = responses[0]
			print tweet.user.screen_name + ' (' + tweet.created_at + ')'
   			print tweet.text.encode('utf-8')
   			print ''

   	if not found:
		print "not found. try again. sry not sry" 

	
#select shorter responses
#order of adjectives


#words = line.split()
#if len(words) == 1:
#	if len(blob.noun_phrases) >= 1:
#		query = blob.noun_phrases[0]
#		query = query + words[1]
#		print query 