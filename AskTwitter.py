#
# getTweets.py
# Created by Catherine Wu and Daphne Weinstein
#
# Usage: python AskTwitter.py
# Then, the user will be prompted to enter a question. Type a question and then press enter. 
# The twitter response will appear in the user's terminal. 
#

from getTweets import returnTweets
from Rewrite import rewriteQuestion
from parseQ import findAnswer
from postprocess import postprocess
from postprocess import postprocessWhoWhereWhat
import urllib3
urllib3.disable_warnings()

# accept a user question and then return a tweet that best answers the question
def main():
 line = raw_input("Enter Question: ")
 firstWord = line.partition(' ')[0]
 wQuestions = ["who", "what", "when", "where", "why"]
 query = ""
 found = False 

 if line.lower() == "what is the meaning of life?":
 	print "42"

 elif firstWord.lower() in wQuestions: 
 	#print "in wQuestions"
 	query = rewriteQuestion(line)

 	plainQuery = query[1:]
 	if query != "none":
 		query = "\"" + query + "\""
 		print(query)
 		allTweets = returnTweets(query)
 		if firstWord.lower() == "who" or firstWord.lower() == "where":
 			#print "postprocessWhoWhere"
 			#print "query is" + plainQuery
 			found = postprocessWhoWhereWhat(allTweets, plainQuery)
 		else:
 			found = postprocess(firstWord.lower(), allTweets, query)
 	if not found:
 		#print "hi"
 		findAnswer(line)

 else: 
 	findAnswer(line)

if __name__ == '__main__':
 main()
