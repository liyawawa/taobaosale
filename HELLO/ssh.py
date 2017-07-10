#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/5 0005 10:38
# @Author  : liya
# @Site    : 
# @File    : ssh.py

# -*- coding: utf-8 -*-

# !/usr/bin/python
import paramiko

def ssh2(ip, username, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            # stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            for o in out:
                print o,
        print '%s\tOK\n' % (ip)
        ssh.close()
    except:
        print '%s\tError\n' % (ip)

if __name__ == '__main__':
    cmd = ['cd tomcat8/;ls']  # 你要执行的命令列表
    username = "root"  # 用户名
    passwd = "pv3gvwnocpk0di0w7ertmfpugwt6W7"  # 密码
    ip = "121.41.53.178"
    print "Begin......"
    ssh2(ip,username,passwd,cmd)


