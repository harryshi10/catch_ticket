#!/usr/bin/env python
# coding=utf-8

# @Author:       harry
# @Time:         2018/1/6 下午12:22
# @Project:      for_fun      
# @File:         catch_ticket.py      
# @Software:     PyCharm

from time import sleep
from splinter.browser import Browser


class CatchTicket(object):
    def __init__(self):
        self.order = 6         # the order of train you want (count from the web top when)

        self.username = u'18701312897'          # your login info on 12306
        self.passwd = u'CraZy03171204'          # your login info on 12306

        self.date = u'2019-01-21'
#        self.from_station = u'%u5317%u4EAC%u897F%2CBXP'  # beijing xi
#        self.to_station = u'%u897F%u5B89%u5317%2CEAY'  # xian bei

        xian_bei_cookie =  u'%u897F%u5B89%u5317%2CEAY'
        beijing_xi_cookie = u'%u5317%u4EAC%u897F%2CBXP'
        self.from_station = beijing_xi_cookie
        self.to_station = xian_bei_cookie

        self.person = [u'石桦', u'陈蕾澌']               # your name here

        self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.login_comp_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.order_submit_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'

        self.driver = Browser(driver_name='chrome')
        self.driver.driver.set_window_size(1400, 1000)

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        self.driver.fill("userDTO.password", self.passwd)
        while self.driver.url != self.login_comp_url:
            print('fill in the certi code yourself...')
            sleep(1)
        print('login complete')

    def start_order(self):
        self.login()
        self.driver.visit(self.search_url)

        self.driver.cookies.add({"_jc_save_fromStation": self.from_station})
        self.driver.cookies.add({"_jc_save_toStation": self.to_station})
        self.driver.cookies.add({"_jc_save_fromDate": self.date})
        self.driver.reload()

        self.driver.find_by_text(u'GC-高铁/城际').click()
        for i in range(2):
            self.driver.find_by_text(u'历时').click()

        count = 1
        while self.driver.url != self.order_submit_url:
            try:
                print('Searching for {} time'.format(count))
                self.driver.find_by_text(u'查询').click()

                if self.driver.find_by_text(u'网络繁忙'):
                    self.driver.find_by_text(u'确认').click()
                else:
                    self.driver.find_by_text(u'预订')[self.order].click()
                sleep(1)
                count += 1
            except Exception as e:
                print(e)
                count += 1
                continue
        print('enter order submit page')
        for name in self.person:
            self.driver.find_by_text(name).last.click()
        try:
            self.driver.find_by_text(u'提交订单').click()
#            self.driver.find_by_text(u'确认').click()
        except Exception as e:
            print(e)
            exit()
        print('order complete')


if __name__ == '__main__':
    catch = CatchTicket()
    catch.start_order()


