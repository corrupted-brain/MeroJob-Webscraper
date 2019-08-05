# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import requests
from bs4 import BeautifulSoup

for y in range(1,5):
	url = "https://merojob.com/search/?page="
	page = requests.get(url=url+str(y))
	for x in range(0,6):
		soup = BeautifulSoup(page.content, 'html.parser')
		main_content=soup.find('div',attrs={'id':'search_job'})
		position=main_content.select('a.no-uline')[x].text.strip()
		orgn=main_content.select('h3.h6')[x].text.strip()
		loc=main_content.select('div',attrs={'class':'media-body'})
		location=soup(itemprop="addressLocality")[x].text.strip()
		deadline=soup.find(itemprop="validThrough").get("content")
		print "\033[1;32;40mJob Role:",position
		print "\033[1;32;40mOrganization:",orgn
		print "\033[1;32;40mJob Location:",location
		print "\033[1;31mDeadline:",deadline
		print "\033[1;36m------------------------"
