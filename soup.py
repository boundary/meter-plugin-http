#!/usr/bin/env python
import threading
from urlparse import urlparse
from urllib import urlopen
from bs4 import BeautifulSoup
from time import time
import sys
import logging


logger = logging.getLogger(__name__)


def worker(img, url):
    """
    thread worker function
    """
    src = img.get('src')
    o = urlparse(src)
    if len(o.netloc) == 0:
        src = url.scheme + '://' + url.netloc + '/' + src
    html = urlopen(src)
    data = html.read()
    logger.debug(html.geturl())
    return


class Soup(object):
    def __init__(self, url):
        self.url = url

    def measure_load_time(self):
        time_begin = time()
        start_url = urlparse(self.url)
        html = urlopen(self.url)
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        threads = []
        for img in bsObj.findAll('img'):
            t = threading.Thread(target=worker, args=(img, start_url))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()
        time_end = time()
        return time_end - time_begin


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("usage: {0} url\n".format(sys.argv[0]))
        exit(1)
    soup = Soup(url=sys.argv[1])
    print(soup.measure_load_time())
