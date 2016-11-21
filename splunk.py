#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import sys
import gzip
import csv
import simplejson

CorpID = "wx5d8053"
Secret = "FOPk4Inz6-_NjeZ9gHN1zJG"

get_AccessToken = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (CorpID, Secret)

req = urllib2.Request(get_AccessToken)

res_data = urllib2.urlopen(req)
res = eval(res_data.read())

token=res["access_token"]

gz = sys.argv[8]

f = gzip.open(gz)
read = csv.reader(f)
for row in read:
    print row[2]
    data = row[2]

foo = sys.argv[3]
print foo

def send_message(msg):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % token
    Header = "Splunk提醒！！"
    values = {"totag": "9","msgtype": "text","agentid": 1,"text": {"content": Header + '\n' + data},"safe":"0"}
    jdata = simplejson.dumps(values, ensure_ascii=False).encode('utf-8') 
    req = urllib2.Request(url, jdata)
    response = urllib2.urlopen(req) 
    return response.read() 

resp = send_message(foo)
print resp



