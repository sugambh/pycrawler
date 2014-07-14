#!/usr/bin/python
#  breadth first search based simple python crawler
import Queue
import re, urllib2

def links_from_page(link):
    # explores the webpage and returns the links on the page as a list
    html=urllib2.urlopen(link).read()
    return re.findall('''href=["'](.[^"']+)["']''',html)

seed=str(raw_input("enter the seed url\n"))
q=Queue.Queue()
q.put(seed)
num=0
while not q.empty():
    url=q.get()
    
    print "number of links processed",num,"\n","crawling page: ",url
    try:
        links=links_from_page(url)
        for link in links:
            if link in q.queue:
                continue
            else:
                q.put(link)
    except:
        print url+" is not a valid url !!"
    num=num+1
        
    
