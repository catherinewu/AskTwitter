# from https://grahamnic.wordpress.com/2013/09/15/python-using-the-twitter-api-to-datamine/

#!/usr/bin/env python
import twitter
import pprint
import argparse

pp = pprint.PrettyPrinter(indent = 4)

api = twitter.Api(
 consumer_key='RtIcNj1NuW7xdysLrhLEc2vk2',
 consumer_secret='bJ1TAEppj8Tr4rYxStRjUCOexDwVpRvSP4F93M760npViepefb',
 access_token_key='3152708877-evAr4YUcBHO8upPo5UbWtRygf0VnpnecVOUXKJz',
 access_token_secret='0baNJ7vqjK66sPMeTulX1utBainbnzrbt22c3pQ6qiq1m'
 )

def returnTweets(searchTerms):
  search = api.GetSearch(term= searchTerms , lang='en', result_type='recent', count=100, max_id='')
  for t in search:
   pp.pprint(t)  
   print t.user.screen_name + ' (' + t.created_at + ')'
   #Add the .encode to force encoding
   print t.text.encode('utf-8')
   print ''


