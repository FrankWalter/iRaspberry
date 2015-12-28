# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json, time
from xml.etree import ElementTree 

# input : 
# output : string set 

def getNews():
	url = 'http://rss.sina.com.cn/news/china/focus15.xml'
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	content = resp.read()
	itemList = ElementTree.fromstring(content).find('channel').findall('item')
	outputList = []
	for item in itemList:
		# news = {}
		# news['title'] = item.find('title').text.encode('utf-8').strip()
		# news['link'] = item.find('link').text.encode('utf-8').strip()[43:]
		# news['pubDate'] = item.find('pubDate').text.encode('utf-8').strip()
		outputList.append(item.find('title').text.encode('utf-8').strip())
		outputList.append(item.find('link').text.encode('utf-8').strip()[43:])
		outputList.append(item.find('pubDate').text.encode('utf-8').strip())

	# return map(lambda x: x['title'] + x['link'] + x['pubDate'], outputList[0: 5])
	return outputList[0: 15]


# for news in getNews():
# 	print news
