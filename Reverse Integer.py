#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2018/11/6 10:10 PM
@Author:  Handsen
@File: Reverse Integer.py
@Software: PyCharm
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = str(x)
            y = int(x[::-1])
        else:
            x = str(abs(x))
            y = -int(x[::-1])
        if (y >= -2 ** 31) and (y <= 2 ** 31 - 1):
            return y
        else:
            return 0
