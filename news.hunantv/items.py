# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DmozItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    link = Field()
    desc = Field()

class BaseBaiduIndexItem(Item):
    name = Field() # tag name
    value = Field() # tag value
    
    
class BaiduIndexItem(Item):
    # define the fields for your item here like:
    # name = Field()
    sex = Field(BaseBaiduIndexItem()) 
    age = Field(BaseBaiduIndexItem())
    job = Field(BaseBaiduIndexItem())
    edu = Field(BaseBaiduIndexItem())
    
    


