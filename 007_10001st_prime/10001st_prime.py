#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project Euler
Problem 7

find the 10001st prime
"""
from numpy import *
def is_prime(num_in):
  """Is number prime

  :num_in: @todo
  :returns: @todo

  """
  ii=2
  while ii <= sqrt(num_in):
    if num_in % ii ==0:
      return False
    ii+=1

  return True

n = 10001
ii=0
jj=2

while ii < n:
  if is_prime(jj):
    ii+=1
  jj+=1

print 'The ',n,'st prime is:',jj-1

