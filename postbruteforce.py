import urllib2
import urllib
#dictionary = 'dictionary.txt'
values={'user':'admin','pass':'password'}
url1='http://darkhat.cf/post.php'
#url2='password'
#url=url1+url2
#response=urllib2.urlopen(url)
#h=response.read()
#print h
data = urllib.urlencode(values)
req = urllib2.Request(url1, data)
response = urllib2.urlopen(req)
h=response.read()
page=h.split('"')
if(page[1] != 'wrong user or password'):
    print 'success'
