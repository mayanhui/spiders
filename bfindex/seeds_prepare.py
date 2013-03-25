# encoding=utf-8
'''
Created on 2012-10-31

@author: mayanhui
'''
import datetime
import sys

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print "You need set the input file path!"
    
    elif len(sys.argv) == 2:
        fpath = '%s' % sys.argv[1]

#    print fpath
    f = open(fpath, "r")  #  Opens file for reading
    
    url_prefix = "http://index.baidu.com/main/word.php?word="
    url_suffix = "&aid="
    
    print "#encoding=gbk"
    print "urls = ["
    
    count = 0
    values = []
    flag = False
    cmp_aid = ""
    for  line  in  f:
        count = count + 1
        now = datetime.datetime.now()
        arr = line.split('\t',-1)
        typeName = arr[0].strip()
        mname = arr[1].strip()
        try:
            mname = mname.decode('utf-8').encode('gbk')
            typeName = typeName.decode('utf-8').encode('gbk')
            print "\"" + url_prefix + mname + url_suffix + typeName + "\","
        except Exception, e:
            continue 
        
    f.close()
    
    print "]"

    
