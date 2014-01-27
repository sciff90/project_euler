#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project Euler
Problem 6
Sum Square Difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""
from numpy import *
n_min = 1
n_max = 100

sum1 = sum(power(range(n_min,n_max+1),2))
sum2 = sum(range(n_min,n_max+1))**2

print 'sum1 = ',sum1
print 'sum2 = ',sum2
print 'diff = ',sum2-sum1
