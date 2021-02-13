# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 上午11:05
# @Author  : void bug
# @FileName: Throttle.py
# @Software: PyCharm
from rest_framework.throttling import UserRateThrottle


class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'


class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'
