# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json, time
from pprint import pprint


city = ""
apikey = ""

with open('config.json', 'r') as f:
    data = json.load(f)
    city = data['city']
    apikey = data['apikey']


url = 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=' + city
req = urllib2.Request(url)
req.add_header("apikey", apikey)
resp = urllib2.urlopen(req)

oOutput = {}
oOutput['update_time'] = time.asctime( time.localtime(time.time()) )

try:
	oResp = json.loads(resp.read())
	oRetData = oResp['retData']
	oOutput['date'] = oRetData['date'].encode('utf-8')
	oOutput['time'] = oRetData['time'].encode('utf-8')
	oOutput['temp'] = oRetData['temp'].encode('utf-8')
	oOutput['l_tmp'] = oRetData['l_tmp'].encode('utf-8')
	oOutput['h_tmp'] = oRetData['h_tmp'].encode('utf-8')
	oOutput['weather'] = oRetData['weather'].encode('utf-8')
	oOutput['city'] = oRetData['city'].encode('utf-8')
	oOutput['status'] = 0
except Exception, e:
	oOutput['status'] = 1
	oOutput['error'] = "some error happened"

with open('output.json', 'w') as f:
	json.dump(oOutput, f, ensure_ascii=False,indent=2,sort_keys=True)






