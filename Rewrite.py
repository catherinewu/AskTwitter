#i'm assuming a list of questions, a multi-line file
import nltk

grammar = r"""
  NP: {<DT|PP\$>?<JJ|JJS>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP|VBN|JJ>+}                # chunk sequences of proper nouns
"""
cp = nltk.RegexpParser(grammar)

questions = open("qs1.txt", "r")

qs = questions.readlines()

for line in qs:
	tokens = nltk.word_tokenize(line)
	tags = nltk.pos_tag(tokens)
	rewrite = ""
	tree = cp.parse(tags)
	print(tree)
	firstnp = False
	npnum = 0
	for subtree in tree.subtrees():
		if subtree.label() == 'NP': 
			npnum = npnum + 1
			if firstnp == False:
				firstnp = True
				for tag in subtree:
					rewrite = rewrite + " " + tag[0]
	if npnum == 1:
		i = 1
		firstwd = nltk.word_tokenize(rewrite)
		print(firstwd[0])
		while tokens[i] != firstwd[0]:
			rewrite = rewrite + " " + tokens[i]
			i = i + 1
		print(rewrite)
	#else push to is-question paradigm



