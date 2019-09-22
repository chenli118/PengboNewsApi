# -*- coding: utf-8 -*-

import re
import time
import requests
import bdpyby
import sys, getopt
from lxml.html import fromstring
from pytube import YouTube

def downpg(html):     
     reg = r"(?<=a\shref=\"/watch).+?(?=\")"
     urlre = re.compile(reg)
     rstr =re.findall(urlre,html) 
     if rstr: 
         dlist =[]
         with open("dlist.txt", 'r') as rf:
             dlist = rf.readlines()
         for wv in rstr:
             ix = wv.index("&amp;list=PL")
             if 10<ix<20:
                 wv=wv[:ix]
             else:
                 continue           
             wv="https://www.youtube.com/watch"+wv
             if wv+'\n' in dlist:
                 continue
             try:
                 YouTube(wv).streams.first().download()
                 with open("dlist.txt", 'a') as af:
                     af.write(wv+"\n")
                 print (wv)      
                 time.sleep(130)
             except:
                 print("down error  "+wv)
             

def downpl(churl):     
    pl_html = requests.get(ch_url).content.decode('utf-8')
    reg = r"(?<=a\shref=\"/playlist).+?(?=\")"
    urlre = re.compile(reg)
    rplstr =re.findall(urlre,pl_html)
    if rplstr and len(rplstr)>0:
        for plurl in rplstr:
            if len(plurl)<20:
                continue
            plurl ="https://www.youtube.com/playlist"+plurl
            vhtml = requests.get(plurl).content.decode('utf-8')
            downpg(vhtml)
    else:
        downpg(pl_html)
    
def downch(churl):
    plurl =churl+"playlists/"
    downpl(plurl)

if __name__ =="__main__":
    ch_url ='https://www.youtube.com/channel/%s/' % (sys.argv[1])
    if len(ch_url)!=57:
        print("请输入正确的频道ID!")
        pass
    else:
        downch(ch_url)
        bdpyby.run()
