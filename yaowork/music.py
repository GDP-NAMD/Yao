import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import requests
from bs4 import BeautifulSoup
url = "http://music.baidu.com/top/dayhot"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)

list_soup = soup.find('div',{'class': 'song-list-wrap'})
for music_info in list_soup.find_all('span',{'class':'song-title '}):
    title = music_info.find('a').string.strip()
    print(title)
