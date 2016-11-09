#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

import sqlite3

conn = sqlite3.connect('weikegu.db')
cursor = conn.cursor()

cursor.execute('CREATE table user ('
               'tmTel varchar(20) primary key,'
               'tmPwd varchar(20),'
               'date varchar(20),'
               'money varchar(20))')

cursor.close()
conn.commit()
conn.close()
