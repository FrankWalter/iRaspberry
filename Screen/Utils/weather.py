# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json, time

city = ""
apikey = ""

# input : 
# output : string 
# weather set :
def getWeather():
	city = "shanghai"
	apikey = "dda2c81ad20ca1e7b506c5696352a9e9"
	url = 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=' + city
	req = urllib2.Request(url)
	req.add_header("apikey", apikey)
	resp = urllib2.urlopen(req)
	oResp = json.loads(resp.read())
	oRetData = oResp['retData']
	weather = oRetData['weather'].encode('utf-8')
	if "晴" in weather :
		return 'sunny'
	elif "雾" == weather:
		return 'fog'
	elif "阴" == weather: 
		return 'overcast'
	elif "雨" in  weather: 
		return 'rain'
	elif "雪" in weather: 
		return 'snow'
	else:
		return 'cloudy'
