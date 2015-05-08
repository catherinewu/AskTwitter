# Run this program to get a tweet that answers a question
from getTweets import returnTweets
from Rewrite import rewriteQuestion
from parseQ import findAnswer

def main():
 line = raw_input("Enter Question: ")
 firstWord = line.partition(' ')[0]
 who = "who"
 what = "what"
 when = "when"
 where = "where"
 why = "why"
 query = ""
 found = False 

 if line.lower() == "what is the meaning of life?":
 	print "42"

 elif firstWord.lower() == who.lower(): 
 	query = rewriteQuestion(line)
 	if query != "":
 		query = "\"" + query + "\""
 		returnTweets(query)

 elif firstWord.lower() == what.lower():
 	rewriteQuestion(line)
 	if query != "":
 		query = "\"" + query + "\""
 		returnTweets(query)

 elif firstWord.lower() == when.lower():
 	rewriteQuestion(line)
 	if query != "":
 		query = "\"" + query + "\""
 		returnTweets(query)

 elif firstWord.lower() == where.lower():
 	rewriteQuestion(line)
 	if query != "":
 		query = "\"" + query + "\""
 		returnTweets(query)

 elif firstWord.lower() == why.lower():
 	rewriteQuestion(line)
 	if query != "":
 		query = "\"" + query + "\""
 		returnTweets(query)

 else: 
 	findAnswer(line)

if __name__ == '__main__':
 main()
