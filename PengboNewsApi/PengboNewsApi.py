import json
import requests
import pymysql
import contextlib
import datetime

def run():
    with mysql() as cursor:
        #url = ('https://newsapi.org/v2/top-headlines?'
        #       'country=us&'
        #       'apiKey=6cae308e2ea846848ea51974adced0fc') 
        url = ('https://newsapi.org/v2/everything?'
               'q=china&'
               'from=2019-09-16&'
               'sortBy=popularity&'
               'apiKey=6cae308e2ea846848ea51974adced0fc')
        response = requests.get(url)
        jstr =response.json() 
        if jstr["status"]=="ok":
            for item in jstr["articles"]:
                for k,v in item.items():
                    if(k=="source"):
                        item[k]=""
                    if(k=="publishedAt"):
                        item[k]=v =str(v)[0:10]
                   
                try:
                    sta = dbinsert(cursor,"pbnews",item)
                except pymysql.err.DataError:
                    print(traceback.print_exc())
                 
def dbinsert(cursor,tbname,dbdict):
    for k,v in dbdict.items():
        if v is str:
            v=v.replace("'","’")
        if isinstance(v,str):
            item[k]=v.replace("'","’")
    columns_string = '(' + ','.join(dbdict.keys()) + ')'
    values_string = "('" + "','".join(map(str, dbdict.values())) + "')"
    sql = """INSERT INTO %s %s VALUES %s""" % (tbname, columns_string, values_string)
    try:
        sta =  cursor.execute(sql)
    except pymysql.err.DataError:
        print(traceback.print_exc())
    if sta and sta == 1:
        return  1
    else:
        return  0

@contextlib.contextmanager
def mysql(host='127.0.0.1', port=3306, user='root', passwd='N3u9.7', db='hanzistock', charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run()