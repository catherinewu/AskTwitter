from textblob import TextBlob

questions = open("qs1.txt", "r")

qs = questions.readlines()

for line in qs:
	print(line)
	blob = TextBlob(line)
	print(blob.noun_phrases)
