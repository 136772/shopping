# coding:utf-8

import requests
import json
import re
import time

class Weikegu(object):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    cookies = ""
    adId = ""
    ha = ""
    # count = ""
    total = ""
    kyjf = ""

    def __init__(self, tmTel, num='124'):
        self.num = num
        self.tmTel = str(tmTel)
        self.tmPwd = '242628'

    def formattime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    def login(self):
        try:
            url = 'http://www.315wkg.com/index.php?s=/Login/login'

            r = requests.get(url, headers=self.headers)
            text = r.text
            self.ha = re.search('name="__hash__" value="(\S+)"', text).group(1)
            #print(self.tmTel, self.ha)
            login_url = 'http://www.315wkg.com/index.php?s=/Login/password/control//tel//gId/'
            payload = {'tmTel': self.tmTel, 'tmPwd': self.tmPwd, '__hash__': self.ha}

            r = requests.post(login_url, data=payload)

            self.cookies = r.cookies
            #print(self.cookies)
            print('[{}]'.format(self.formattime()),self.tmTel, '登录成功')
            return self.shopping()
            #
            #r = requests.get('http://www.315wkg.com/index.php?s=/My/index', cookies=self.cookies)
            #print(self.tmTel,r)
        except Exception as e:
            return '失败', self.tmTel, e

    def shopping(self):
        try:
            url = 'http://www.315wkg.com/index.php?s=/Shoppingcart/billing/gId/{}/gNum/1'.format(self.num)
            # print(url)
            r = requests.get(url, cookies=self.cookies, headers=self.headers)

            text = r.text
            self.adId = re.search('name="adId" value="(\d+)"', text).group(1)
            self.ha = re.search('name="__hash__" value="(\S+)"', text).group(1)
            # self.count = re.search('name="{}" value="(\d+)"'.format(self.num), text).group(1)
            self.total = re.search('name="total" value="(\d+)"', text).group(1)
            self.kyjf = re.search('<div class="kyjf">可用积分：<span>(\d+)</span>', text).group(1)

            # print(text)
            if int(self.kyjf) >= int(self.total):
                print('[{}]'.format(self.formattime()),self.tmTel, '购物前余额:', self.kyjf, '添加购物车成功')
                return self.paying()

            else:
                return '余额不足',self.tmTel,self.kyjf
        except Exception as e:
            return '失败',self.tmTel,e

    def paying(self):
        try:
            # print(self.num)
            url = 'http://www.315wkg.com/index.php?s=/Settlement/settlement'
            payload = {
                'adId': self.adId,
                '{}'.format(self.num): '1',
                'total': self.total,
                '__hash__': self.ha,
            }
            # print(payload)
            r = requests.post(url, data=payload, cookies=self.cookies, headers=self.cookies)

            text = r.text
            temp = re.findall("alert\([\'\"](.*)[\'\"]\);", text)
            if temp:
                return temp[0], self.tmTel,""
            else:
                temp = re.findall('window.location="(\S+)";', text)

                payurl = 'http://www.315wkg.com' + temp[0]
                r = requests.get(payurl, cookies=self.cookies, headers=self.cookies)
                if r.status_code != requests.codes.ok:
                    payurl = 'http://www.315wkg.com/index.php?s=' + temp[0]
                    r = requests.get(payurl, cookies=self.cookies, headers=self.cookies)
                    text = r.text
                temp = re.findall("alert\([\'\"](.*)[\'\"]\);", text)
                if temp:
                    return temp[0], self.tmTel,self.kyjf
                
        except Exception as e:
            return '失败', self.tmTel, e



if __name__ == '__main__':
    weikegu = Weikegu('13001938805')
    print(weikegu.login())
