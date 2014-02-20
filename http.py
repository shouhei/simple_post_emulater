# coding:utf-8
import urllib
import urllib2
import json
import sys

args = sys.argv
argc = len(args)
if (argc != 3):
    print 'Usage: arg is url and filename'
    quit();


url    = args[1]
print url
params = json.load(open(args[2]))
print params
params = urllib.urlencode(params)

req = urllib2.Request(url)
# ヘッダ追加
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
# パラメータ追加 
req.add_data(params)

res = urllib2.urlopen(req)

# レスポンス取得
body = res.read()
print json.loads(body);

