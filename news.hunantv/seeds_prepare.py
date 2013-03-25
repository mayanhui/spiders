# encoding=utf-8
'''
Created on 2012-10-31

@author: mayanhui
'''
import datetime
import sys
import urllib, urllib2, cookielib
from scrapy.selector import HtmlXPathSelector
# from BeautifulSoup import BeautifulSoup

if __name__ == "__main__":
    
#    if len(sys.argv) == 1:
#        print "You need set the input file path!"
#    
#    elif len(sys.argv) == 2:
#        date = '%s' % sys.argv[1]
        
    now = datetime.datetime.now().strftime('%Y%m%d')
#    print  now
        
    print "urls = ["  
    url = "http://www.hunantv.com/movie/news/"
    urllib2.socket.setdefaulttimeout(30)
    html_src = urllib2.urlopen(url).read()

    arr = html_src.split('\n', -1)
    for line in arr:
        arr2 = line.split("<a", -1)
        for line2 in arr2:
            if line2.find("http://www.hunantv.com/c") != -1:
                str = "\"" + line[line.find("http://www.hunantv.com/c"):line.find(".html") + len(".html")] + "\","
                print str
            
    print "]"

    
