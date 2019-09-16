import requests
import re
from lxml.html import fromstring

def writeword(url):   
    #rec = re.compile('<pre>([^<]*)</pre>')//table width="40%"
    html = requests.get(url).content.decode('utf-8')
    htext = fromstring(html)
    rows =  htext.xpath("//table[@width=\"40%\"]/tr") 
    if rows:
        with open("001.txt", 'a') as f:
            for row in rows:
                tds =list(filter(None,row.text_content().replace('\t','').split('\n')))
                if len(tds)==2:
                    if tds[0].isdigit():                     
                        f.write("\n"+tds[0]+"\t"+tds[1]) 

def run():
    for i in range(21,61):
        url ='http://www.naturalenglish.club/esl/%s00.php' %(i)
        try:
            writeword(url)
            print("sucess:"++url)
        except:
            print("error:"+url)
        
if __name__ =="__main__":
    run()
