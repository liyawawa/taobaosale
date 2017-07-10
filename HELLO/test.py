#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/5 0005 17:13
# @Author  : liya
# @Site    : 
# @File    : test.py
import dataSource
from sql import Mysql
import time

mysql = Mysql()


sqlAll = "insert into taobaoSale(`itemId`,`link`,`title`,`subtitle`,`intro`,`imagePath`,`staticImgPath`,`imagePaths`,`sellPrice`,`price`,`itemUrl`,`descUrl`,`planUrl`,`ulandUrl`,`historySales`,`viewCount`,`sellerId`,`sellerType`,`sellerName`,`flagShip`,`certIcon`,`cpId`,`cpPrice`,`cpSpare`,`cpCount`,`cpTotal`,`cpCondition`,`cpLimit`,`cpStarts`,`cpExpired`,`cpLevel`,`cpUrl`,`gold`,`ju`,`qiang`,`freeExpress`,`freeExpressBack`,`commission`,`cgold`,`goodRatePercentage`,`dx`,`is_brand`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

i = 119
while i <= 708:
    param = dataSource.getData(i)
    result = mysql.insertMany(sqlAll, param)
    mysql.end()
    i = i + 1
    print i
    time.sleep(3)


mysql.dispose()
# jsonss = json.loads(jsons['list'][1:-1])
# print jsonss
