import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import requests
from bs4 import BeautifulSoup
url = "http://www.douban.com/tag/%E4%BA%BA%E7%89%A9%E4%BC%A0%E8%AE%B0/book"
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)

list_soup = soup.find('div',{'class': 'mod book-list'})
for book_info in list_soup.find_all('dd'):
    print(book_info.find('a',{'class':'title'}).string.strip())
