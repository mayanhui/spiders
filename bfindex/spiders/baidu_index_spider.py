#encoding=gbk
'''
Created on 2012-10-30

@author: root
'''
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from lxml import etree

import urllib2

import re
import string

from bfindex import seeds


class BaiduIndexSpider(BaseSpider):
    name = "baidu.index"
    allowed_domains = ["index.baidu.com"]
    
    
    start_urls = seeds.urls

    malePattern = re.compile('male:"(.+)"')
    femalePattern = re.compile('female:"(.+)"')
    def parse(self, response):
        pair = response.url.replace("http://index.baidu.com/main/word.php?word=","").strip().split("&aid=")
        
#        aid = pair[1].strip()
        aid = urllib2.unquote(pair[1].strip()).decode('gbk').encode('utf-8')
        aname = urllib2.unquote(pair[0]).decode('gbk').encode('utf-8')
        
        #print aname
        
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[contains(@class, "boxBody")]')

        for site in sites:
            sitehtml = site.extract()
            if(string.find(sitehtml,"male:")>=0 and string.find(sitehtml,"female:") >= 0):
                #sex
                sex = site.select('//script[contains(@language, "javascript")]').extract()
                
                maleMatch = self.malePattern.search(sex[1])
                malePercentage = '0';
                femalePercentage ='0'
                if maleMatch:
                    malePercentage= maleMatch.group(1)
                femaleMatch = self.femalePattern.search(sex[1])
                if femaleMatch:
                    femalePercentage = femaleMatch.group(1)
                    
                print aid,"\t",aname,'\tsex','male',malePercentage,malePercentage
                
                print aid,"\t",aname,'\tsex','female',femalePercentage,femalePercentage
                
                #age
                tables = site.select('//table')
                for table in tables:
                    tablehtml = table.extract()
                    if(string.find(tablehtml,"10-19")>=0):
                        tbl = etree.fromstring(tablehtml)
                        children = list(tbl)
                        sum = float(0.0)
                        for child in children:
                            name = child[1].text
                            value = ""
                            for c in list(child[2]):
                                value = c.xpath('@style')
                            if("None" == name or value == ""):
                                continue
                            value = value[0].replace("width:","").replace("%;","").strip()
                            sum = sum + float(value)
                        
                        for child in children:
                            name = child[1].text
                            value = ""
                            for c in list(child[2]):
                                value = c.xpath('@style')
                            if("None" == name or value == ""):
                                continue
                            value = value[0].replace("width:","").replace("%;","").strip()
                            pvalue = float('%.2f'% (float(value)/sum * 100))
                            
                            print aid,"\t",aname,'\tage',name.encode("utf-8"),value,pvalue
                    #job  
                    elif(string.find(tablehtml,"IT")>=0):
                        tbl = etree.fromstring(tablehtml)
                        children = list(tbl)
                        sum = float(0.0)
                        for child in children:
                            name = child[1].text
                            value = ""
                            for c in list(child[2]):
                                value = c.xpath('@style')
                            if("None" == name or value == ""):
                                continue
                            value = value[0].replace("width:","").replace("%;","").strip()
                            sum = sum + float(value)
                        
                        for child in children:
                            name = child[1].text
                            value = ""
                            for c in list(child[2]):
                                value = c.xpath('@style')
                            if("None" == name or value == ""):
                                continue
                            value = value[0].replace("width:","").replace("%;","").strip()
                            pvalue = float('%.2f'% (float(value)/sum * 100))
                            
                            print aid,"\t",aname,'\tjob',name.encode("utf-8"),value,pvalue
                    #edu
                    elif(string.find(tablehtml,"tdkey")>=0):
                        tbl = etree.fromstring(tablehtml)
                        children = list(tbl)
                        sum = float(0.0)
                        for child in children:
                            name = child[1].text
                            value = ""
                            for c in list(child[2]):
                                value = c.xpath('@style')
                            if("None" == name or value == ""):
                                continue
                            value = value[0].replace("width:","").replace("%;","").strip()
                            sum = sum + float(value)
                        
                        for child in children:
                            name = child[1].text
                            value = ""
                            for c in list(child[2]):
                                value = c.xpath('@style')
                            if("None" == name or value == ""):
                                continue
                            value = value[0].replace("width:","").replace("%;","").strip()
                            pvalue = float('%.2f'% (float(value)/sum * 100))
                             
                            print aid,"\t",aname,'\tedu',name.encode("utf-8"),value,pvalue
               
                break
            
