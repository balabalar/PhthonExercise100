# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/19-9:30 AM
@file: eatPeach.py
@function: 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
a = 1
for i in range(2,11):
    a = (a + 1) * 2
    print("第{}天吃了{}个桃子".format(i,a))
