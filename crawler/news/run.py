# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json, time
from pprint import pprint


with open('config.json', 'r') as f:
    data = json.load(f)
    city = data['city']
    apikey = data['apikey']


url = 'http://news.qq.com/newsgn/rss_newsgn.xml'
req = urllib2.Request(url)
resp = urllib2.urlopen(req)

oOutput = {}
oOutput['update_time'] = time.asctime( time.localtime(time.time()) )

try:
	data = resp.read()
	# oResp = json.loads(resp.read())
	print data

	
except Exception, e:
	oOutput['status'] = 1
	oOutput['error'] = "some error happened"
else:
	oOutput['status'] = 0
	oOutput['error'] = ""


with open('output.json', 'w') as f:
	json.dump(oOutput, f, ensure_ascii=False,indent=2,sort_keys=True)






