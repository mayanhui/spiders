#!/bin/bash

source /etc/profile

PYTHON27_HOME=/opt/modules/python2.7/bin
PROJECT_HOME=/opt/modules/scrapy/bfindex-spiders
DATA_HOME=/opt/modules/scrapy/data

#Prepare seed.py
echo "Get type_name-mname from hive..."
echo "remove file ${DATA_HOME}/type_mname.tsv"
rm -rf ${DATA_HOME}/type_mname.tsv

/opt/modules/hive/hive-0.9.0/bin/hive -e"set mapred.job.queue.name=ETL;select if(type_name is not null and type_name != \"\", type_name,\"其他\"),mname from baofengindex.bf_index_vv_play_album_history group by type_name,mname" > ${DATA_HOME}/type_mname.tsv

echo "Generate seeds.py..."
echo "remove file ${PROJECT_HOME}/bfindex/seeds.py*"
rm -rf ${PROJECT_HOME}/bfindex/seeds.py*

${PYTHON27_HOME}/python2.7 ${PROJECT_HOME}/bfindex/seeds_prepare.py ${DATA_HOME}/type_mname.tsv > ${PROJECT_HOME}/bfindex/seeds.py


echo "Crawling..."
echo "remove file ${DATA_HOME}/bf_index_vv_play_album_crowd_attrs.txt"
rm -rf ${DATA_HOME}/bf_index_vv_play_album_crowd_attrs.txt

${PYTHON27_HOME}/scrapy crawl baidu.index > ${DATA_HOME}/bf_index_vv_play_album_crowd_attrs.txt

echo "Load data into MYSQL..."
${PYTHON27_HOME}/python2.7 ${PROJECT_HOME}/bfindex/dao.py ${DATA_HOME}/bf_index_vv_play_album_crowd_attrs.txt

echo "Done!"
