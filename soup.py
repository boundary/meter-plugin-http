#!/usr/bin/env python
import threading
from urlparse import urlparse
from urllib import urlopen
from bs4 import BeautifulSoup
from time import time
url = 'http://web-1/index.html'
url = 'http://www.bmc.com'
start_url = urlparse(url)
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'html.parser')

def worker(img):
    """
    thread worker function
    """
    src = img.get('src')
    o = urlparse(src)
    print(o)
    print(type(0))
    if len(o.netloc) == 0:
        src = start_url.scheme + '://' + start_url.netloc + '/' + src
    html = urlopen(src)
    data = html.read()
    print(html.geturl())
    return

class Soup(object):

    def __init__(self, url):
	self.url = url

threads=[]
time_begin = time()
for img in bsObj.findAll('img'):
    t = threading.Thread(target=worker, args=(img,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
time_end = time()
print(time_end - time_begin)
