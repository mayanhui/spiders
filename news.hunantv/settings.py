# Scrapy settings for dmoz project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'news-hunantv'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['news-hunantv.spiders']
NEWSPIDER_MODULE = 'news-hunantv.spiders'
DEFAULT_ITEM_CLASS = 'news-hunantv.items.DmozItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

