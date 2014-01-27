#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project euler multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from numpy import *

N = 1000
m1 = 3
m2 = 5

ss = 0

for ii in range(1,N):
  if ii%m1==0 or ii%m2==0:

    ss+=ii
print 'For multiples of ',m1,' and ',m2,' for numbers between 1 and ',N
print 'Sum is: ',ss
