######CMS Crawler###########
#import Beautiful_Soup
import urllib
from bs4 import BeautifulSoup
#from BeautifulSoup import *
#x=raw_input("enter url");
xml =urllib.urlopen('http://cms.bits-hyderabad.ac.in/bits-cms/course/index.php').read()
soup = BeautifulSoup(xml,'html.parser')
#print(soup.prettify());
#import urllib

l=list();
for link in soup.find_all('a'):
	x=link.get('href')
	if x.startswith('#'):
		continue
	elif x in l:
		continue
	else:
		l.append(x)
	for x in l:
		print x

for url in l:
	xml=urllib.urlopen(url).read()
	soup = BeautifulSoup(xml,'html.parser')
	for link in soup.find_all('a'):
		x=link.get('href')
		#if x.startswith('#'):
		#	continue
		if x in l:
			continue
		else:
			y=0
    		l.append(x)
    	for x in l:
    		print x


for x in l:
	print x
