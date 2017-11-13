# -*- coding: utf-8 -*-
import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="dd")
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            sql = "insert goods(title,link,comment) values('" + title + "','" + link + "','" + comment + "')"
            try:
                conn.query(sql)
            except Exception as err:
                print(err)
        conn.close()
        return item
