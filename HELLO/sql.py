#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/7 0007 10:45
# @Author  : liya
# @Site    : 
# @File    : sql.py

import MySQLdb
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
# from PooledDB import PooledDB
import Config

"""
Config是一些数据库的配置文件
"""


class Mysql(object):
    """
MYSQL数据库对象，负责产生数据库连接, 此类中的连接采用连接池实现获取连接对象：conn = Mysql.getConn()
释放连接对象;
conn.close()
或del
conn
"""


    # 连接池对象
    __pool = None


    def __init__(self):
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self._conn = Mysql.__getConn()
        self._cursor = self._conn.cursor()


    @staticmethod
    def __getConn():
        if Mysql.__pool is None:
            __pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,
                              host=Config.DBHOST, port=Config.DBPORT, user=Config.DBUSER, passwd=Config.DBPWD,
                              db=Config.DBNAME, use_unicode=False, charset=Config.DBCHAR, cursorclass=DictCursor)
        return __pool.connection()

    def insertOne(self, sql, value):
        """ 
        @summary: 向数据表插入一条记录 
        @param sql:要插入的ＳＱＬ格式 
        @param value:要插入的记录数据tuple/list 
        @return: insertId 受影响的行数 
        """
        count = self._cursor.execute(sql, value)
        return count


    def insertMany(self, sql, values):
        """ 
            @summary: 向数据表插入多条记录 
            @param sql:要插入的ＳＱＬ格式 
            @param values:要插入的记录数据tuple(tuple)/list[list] 
            @return: count 受影响的行数 
        """
        count = self._cursor.executemany(sql, values)
        return count

    def begin(self):
        """ 
        @summary: 开启事务 
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """ 
        @summary: 结束事务 
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """ 
            @summary: 释放连接池资源 
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback');
        self._cursor.close()
        self._conn.close()