#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 5
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
def divisable_all(num_in,n1,n2):
  """is number divisable by all numbers in range n1 to n2

  :num_in: @todo
  :returns: @todo

  """
  for ii in range(n1,n2):
    if num_in % ii !=0:
      return False

  return True


num1 = 1
num2 = 20
ii=1

while 1:
  if divisable_all(ii,num1,num2):
    break
  ii+=1

print 'Smallest number divisible by numbers from ',num1,' to ',num2,': ',ii

