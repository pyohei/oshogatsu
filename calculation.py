#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
calculate last day of this yeaer.
This module need not argment.

Created 2014/05/20
"""

from datetime import date

class Calculation(object):

    def __init__(self):
        self.my_today = date.today()

    def calc_rest_day(self):
        my_today = self.my_today
        y = my_today.year
        rest_day = date(y+1, 1, 1) - my_today
        return rest_day.days

    def calc_passed_rate(self):
        my_today = self.my_today
        y = my_today.year
        a_year = date(y+1, 1, 1) - date(y, 1, 1)
        until_today = my_today - date(y, 1, 1)
        return round(
            ((until_today.days * 1.0 / a_year.days) 
            * 100.0), 2)


if __name__ == '__main__':
    c = Calculation()
    print(c.calc_rest_day())
    print(c.calc_passed_rate())
