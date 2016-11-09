#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
import model

db = model.DbControl()

datalist = db.datareport()

print(datalist)
for i in datalist:
    print('\033[1;32;m {} \033[0m'.format(i.tmTel))
