#!/usr/bin/python
# -*- coding: utf-8 -*-
#Auther:xwjr.com
import urllib2,sys,gzip,csv,json

CorpID = "wx5d814254ec559053"
Secret = "FOPk4InFkBg1ju6_MwYqKrLtXaAQbR7GD_8QgtpaNlayvHFdz6-_NjeZ9gHN1zJG"
ToTag = "9"
AgentID = "1"
get_AccessToken = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (CorpID, Secret)

req = urllib2.Request(get_AccessToken)
response_data = urllib2.urlopen(req)
res = eval(response_data.read())
Token=res["access_token"]



GzipFile = sys.argv[8]
CsvFile = gzip.open(GzipFile)
CsvRead = csv.reader(CsvFile)
for row in CsvRead:
    SplunkLogInfo = row[2]

def SendMessage(SplunkLogInfo,ToTag,AgentID):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Header = "splunk提醒！！"
    values = {"totag": ToTag,"msgtype": "text","agentid": AgentID,"text": {"content": Header + '\n' + SplunkLogInfo},"safe":"0"}
    jdata = json.dumps(values, ensure_ascii=False)
    req = urllib2.Request(url, jdata)
    response = urllib2.urlopen(req) 
    return response.read() 

Response = SendMessage(SplunkLogInfo,ToTag,AgentID)
print Response



