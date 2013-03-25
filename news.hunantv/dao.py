#encoding=utf-8
'''
Created on 2012-10-31

@author: mayanhui
'''
import MySQLdb
import datetime
import sys

class BfindexDaoClass(object):
    '''
    classdocs
    '''
    def select(self):
        conn = MySQLdb.connect(host='192.168.2.60', user='root',passwd='binma85')  
        cursor = conn.cursor()  
        conn.select_db('bfindex');  
        #执行SQL,创建一个数据表. 
        cursor.execute("set names utf8")
        count = cursor.execute("select * from bfindex.bf_index_vv_play_album_history limit 10")  
  
        print count
        results = cursor.fetchall()  
        for r in results:  
            print r[0],r[1],r[2],r[3] 
        conn.close()
        
    def insert(self,value):
#        conn = MySQLdb.connect(host='114.112.70.42', user='admin',passwd='223238')
        conn = MySQLdb.connect(host='192.168.2.60', user='root',passwd='binma85') 
        cursor = conn.cursor()  
        conn.select_db('bfindex');  

        cursor.execute("set names utf8")
        cursor.execute("insert into bfindex.bf_index_vv_play_album_crowd_attrs(type_name,mname,attr,type,width_value,percent_value,stat_date) values(%s,%s,%s,%s,%s,%s)",value)  
        
        conn.close() 
         
    def bulk_insert(self,values):
#        conn = MySQLdb.connect(host='114.112.70.42', user='admin',passwd='223238')
        conn = MySQLdb.connect(host='192.168.2.60', user='root',passwd='binma85') 
        cursor = conn.cursor()  
        conn.select_db('bfindex');  

        cursor.execute("set names utf8")
        cursor.executemany("insert into bfindex.bf_index_vv_play_album_crowd_attrs(type_name,mname,attr,type,width_value,percent_value,stat_date) values(%s,%s,%s,%s,%s,%s,%s)",values)  
        
        conn.commit()
        cursor.close()
        conn.close()
    

    def __init__(self):
        '''
        Constructor
        '''
        self = self

if __name__ == "__main__":
    dao = BfindexDaoClass()
    #dbc.select()
    
    if len(sys.argv)==1:
        print "You need set the input file path!"
    
    elif len(sys.argv)==2:
        fpath='%s' % sys.argv[1]

    print fpath
    f = open(fpath, "r" )  #  Opens file for reading
    
    count = 0
    values = []
    flag = False
    cmp_aid = ""
    for  line  in  f:
        count = count + 1
        now = datetime.datetime.now()
        if(count % 100 == 0):
            dao.bulk_insert(values)
            print (now,"Insert ", count, "lines!")
            values = []
        arr = line.split('\t')
        typeName = arr[0].strip()
        mname = arr[1].strip()
        
        attrs = arr[2].split(' ')
        attr = attrs[0].strip()
        type = attrs[1].strip()
        width_value = attrs[2].strip()
        percent_value = attrs[3].strip()
        
        stat_date = now.strftime('%Y-%m-%d')
        value = [typeName,mname,attr,type,width_value,percent_value,now]
        values.append(value)
        
    f.close()

    