#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/5 0005 17:13
# @Author  : liya
# @Site    : 
# @File    : insertdate.py
import threading

from _mysql_exceptions import IntegrityError

import dataSource
from sql import Mysql
import time

def insert():

    mysql = Mysql()
    sqlAll = "insert into taobaoSale(`itemId`,`link`,`title`,`subtitle`,`intro`,`imagePath`,`staticImgPath`,`imagePaths`,`sellPrice`,`price`,`itemUrl`,`descUrl`,`planUrl`,`ulandUrl`,`historySales`,`viewCount`,`sellerId`,`sellerType`,`sellerName`,`flagShip`,`certIcon`,`cpId`,`cpPrice`,`cpSpare`,`cpCount`,`cpTotal`,`cpCondition`,`cpLimit`,`cpStarts`,`cpExpired`,`cpLevel`,`cpUrl`,`gold`,`ju`,`qiang`,`freeExpress`,`freeExpressBack`,`commission`,`cgold`,`goodRatePercentage`,`dx`,`is_brand`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cate = ['7','2','1','9','8','5','10','4','6','3','99']

    for cateid in cate:
        print cateid

        i = 1
        while True:
            print '------当前进度--------：第%s页' % i
            param = dataSource.getData(i,cateid,mysql)
            i = i + 1
            if param == ['none']:
                print '--------当前%s页为终结页' % (i-1)
                break
            else:
                try:
                    result = mysql.insertMany(sqlAll, param)
                    mysql.end()
                except IntegrityError:
                    print '--------warn当前%s页出现异常' % i
                    continue
                finally:
                    # 续1s
                    time.sleep(1)
    mysql.dispose()

    global timer
    timer = threading.Timer(43200, insert)
    timer.start()



if __name__ == '__main__':

    timer = threading.Timer(1, insert)
    timer.start()
    insert()

