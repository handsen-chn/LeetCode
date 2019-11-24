#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2018/11/6 9:05 PM
@Author:  Handsen
@File: Two Sum.py
@Software: PyCharm
"""


# 自己写的，简直感人，击败8%的提交者
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]


# 别人的写法，使用字典，数据存储，存储比较同时进行
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]
