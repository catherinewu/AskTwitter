#
# getTweets.py
# Created by Catherine Wu and Daphne Weinstein
#
# Queries the Twitter API with specified searchTerms and returns 10 tweets
#

#!/usr/bin/env python
import twitter
import pprint
import argparse
import urllib3
urllib3.disable_warnings()

#pp = pprint.PrettyPrinter(indent = 4)

api = twitter.Api(
 consumer_key='RtIcNj1NuW7xdysLrhLEc2vk2',
 consumer_secret='bJ1TAEppj8Tr4rYxStRjUCOexDwVpRvSP4F93M760npViepefb',
 access_token_key='3152708877-evAr4YUcBHO8upPo5UbWtRygf0VnpnecVOUXKJz',
 access_token_secret='0baNJ7vqjK66sPMeTulX1utBainbnzrbt22c3pQ6qiq1m'
 )

# Queries the Twitter API with searchTerms and returns 10 tweets
def returnTweets(searchTerms):
  search = api.GetSearch(term= searchTerms , lang='en', result_type='recent', count=10, max_id='')
  return search
  #print type(search)
  #for t in search:
   #pp.pprint(t)  
   #print t.user.screen_name + ' (' + t.created_at + ')'
   ##Add the .encode to force encoding
   #print t.text.encode('utf-8')
   #print ''

