import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import requests
from bs4 import BeautifulSoup
url = "http://www.1905.com/vod/cctv6/lst/week"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)
count="%10s\t%10s\t%10s\n"%("title","score","information")
list_soup = soup.find('div',{'class': 'container'})
for movie in list_soup.find_all('section',{'class':'mod'}):
    for movie_info in movie.find_all('div',{'class':'grid-2x'}):
        title = movie_info.find('h3').string.strip()
        score = movie_info.find('b').string.strip()
        info = movie_info.find('p').string.strip()
        count += "%8s\t%8s\t%8s\n"%(title,score,info)
print(count)
