#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/5 0005 17:13
# @Author  : liya
# @Site    : 
# @File    : test.py
from _mysql_exceptions import IntegrityError

import dataSource
from sql import Mysql
import time

mysql = Mysql()


sqlAll = "insert into taobaoSale(`itemId`,`link`,`title`,`subtitle`,`intro`,`imagePath`,`staticImgPath`,`imagePaths`,`sellPrice`,`price`,`itemUrl`,`descUrl`,`planUrl`,`ulandUrl`,`historySales`,`viewCount`,`sellerId`,`sellerType`,`sellerName`,`flagShip`,`certIcon`,`cpId`,`cpPrice`,`cpSpare`,`cpCount`,`cpTotal`,`cpCondition`,`cpLimit`,`cpStarts`,`cpExpired`,`cpLevel`,`cpUrl`,`gold`,`ju`,`qiang`,`freeExpress`,`freeExpressBack`,`commission`,`cgold`,`goodRatePercentage`,`dx`,`is_brand`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

i = 1
while True:
    cate = 8
    print '------当前进度--------：第%s页' % i
    param = dataSource.getData(i,cate)
    i = i + 1

    if len(param) == 0:
        print '--------当前%s页为终结页' % (i-1)
        break
    else:
        # 异常除去重复数据
        try:
            result = mysql.insertMany(sqlAll, param)
            mysql.end()
        except IntegrityError:
            print '--------warn当前%s页出现异常' % i
            continue
        finally:
            time.sleep(1)

mysql.dispose()
# jsonss = json.loads(jsons['list'][1:-1])
# print jsonss
