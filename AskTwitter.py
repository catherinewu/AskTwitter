# Run this program to get a tweet that answers a question
from getTweets import returnTweets
from Rewrite import rewriteQuestion
from parseQ import findAnswer
from postprocess import postprocess
import urllib3
urllib3.disable_warnings()

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
 	#print type(query)
 	if query != "none":
 		query = "\"" + query + "\""
 		allTweets = returnTweets(query)
 		found = postprocess(firstWord.lower(), allTweets)
 	if not found:
 		#print "hi"
 		findAnswer(line)

 elif firstWord.lower() == what.lower():
 	rewriteQuestion(line)
 	if query != "none":
 		query = "\"" + query + "\""
 		allTweets = returnTweets(query)
 		found = postprocess(firstWord.lower(), allTweets)
 	if not found: 
 		findAnswer(line)

 elif firstWord.lower() == when.lower():
 	rewriteQuestion(line)
 	if query != "none":
 		query = "\"" + query + "\""
 		allTweets = returnTweets(query)
 		found = postprocess(firstWord.lower(), allTweets)
 	if not found:
 		findAnswer(line)

 elif firstWord.lower() == where.lower():
 	rewriteQuestion(line)
 	if query != "none":
 		query = "\"" + query + "\""
 		allTweets = returnTweets(query)
 		found = postprocess(firstWord.lower(), allTweets)
 	if not found:
 		findAnswer(line)

 elif firstWord.lower() == why.lower():
 	rewriteQuestion(line)
 	if query != "none":
 		query = "\"" + query + "\""
 		allTweets = returnTweets(query)
 		found = postprocess(firstWord.lower(), allTweets)
 	if not found:
 		findAnswer(line)

 else: 
 	findAnswer(line)

if __name__ == '__main__':
 main()
