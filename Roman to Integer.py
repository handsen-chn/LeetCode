# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Roman to Integer
   Description :
   Author :       yinjun8
   date：          2018/12/20
-------------------------------------------------
   Change Activity:
                   2018/12/20:
-------------------------------------------------
"""
__author__ = 'yinjun8'


# 自己的写的第一个，时间超出
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        initial = 0
        i = 0
        sl = list(s)
        length = len(sl)
        while (i <= length - 1):
            if sl[i] == 'I':
                if i < length - 1:
                    if sl[i + 1] == 'V':
                        result = 4
                        i = i + 2
                    elif sl[i + 1] == 'X':
                        result = 9
                        i = i + 2
                    else:
                        result = 1
                        i = i + 1
                elif sl[i] == 'V':
                    result = 5
                elif sl[i] == 'X':
                    if i < length - 1:
                        if sl[i + 1] == 'L':
                            result = 40
                            i = i + 2
                        elif sl[i + 1] == 'C':
                            result = 90
                            i = i + 2
                        else:
                            result = 10
                            i = i + 1
                elif sl[i] == 'L':
                    result = 50
                elif sl[i] == 'C':
                    if i < length - 1:
                        if sl[i + 1] == 'D':
                            result = 400
                            i = i + 2
                        elif sl[i + 1] == 'M':
                            result = 900
                            i = i + 2
                        else:
                            result = 100
                            i = i + 1
                elif sl[i] == 'D':
                    result = 500
                    i = i + 1
                else:
                    result = 1000
                    i = i + 1
        initial = initial + result
        return initial


# 自己写的第二个，通过
class Solution:
    def romanToInt(self, s):
        ss = list(s)
        length = len(ss)
        # all_sub_string = [s[i:j+1]  for i in xrange(length) for j in xrange(i,length)]
        # all_sub_string = [s[i:i+2]  for i in xrange(length-1)]
        target_normal = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value_normal = [1, 5, 10, 50, 100, 500, 1000]
        target = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        value = [4, 9, 40, 90, 400, 900]
        i = 0
        initial = 0
        while (i <= length - 1):
            if i < length - 1:
                m = ss[i] + s[i + 1]
                if m in target:
                    result = value[target.index(m)]
                    i = i + 2
                else:
                    result = value_normal[target_normal.index(ss[i])]
                    i = i + 1
            else:
                result = value_normal[target_normal.index(ss[i])]
                i = i + 1
            initial = initial + result
        return initial
