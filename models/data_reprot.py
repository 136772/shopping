#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
import model

db = model.DbControl()

datalist = db.datareport()
moneylist = db.checkmoney()
def todaycard():
    count=1
    screen_width=80
    text_width=14
    box_width=text_width+6
    left_margin=(screen_width-box_width)//2
    print('\033[1;32;m ')
    print(' '*left_margin,'已抢卡列表',' '*(text_width+2))
    print(' '*left_margin+'+'+'-'*(text_width+2)+ '+')
    print(' '*left_margin+'|'+' '*(text_width+2)+  '|')

    for i in datalist:
        print(' ' * left_margin + '|' + '{}. {}'.format(count, i.tmTel) + ' ' * (box_width - text_width - 4) + '|')
        count+=1

    print(' '*left_margin+'|'+' '*(text_width+2)+  '|')
    print(' '*left_margin+'+'+'-'*(text_width+2)+ '+')
    print()
    print(' \033[0m')
    return


def nomoney():
    count=1
    screen_width=80
    text_width=22
    box_width=text_width+6
    left_margin=(screen_width-box_width)//2
    print('\033[1;32;m ')
    print(' '*left_margin,'无余额列表',' '*(text_width+2))
    print(' '*left_margin+'+'+'-'*(text_width+2)+ '+')
    print(' '*left_margin+'|'+' '*(text_width+2)+  '|')

    for i in moneylist:
        if int(i.money)<3000:
            print(' ' * left_margin + '|' + '{}. {} 余额:{}'.format(count, i.tmTel, i.money) + ' ' * (box_width - text_width - 4) + '|')
            count+=1

    print(' '*left_margin+'|'+' '*(text_width+2)+  '|')
    print(' '*left_margin+'+'+'-'*(text_width+2)+ '+')
    print()
    print(' \033[0m')
    return

todaycard()
nomoney()
