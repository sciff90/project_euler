#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project euler problem 3
Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from numpy import *

def is_prime(num_in):
  """Returns a true if number is prime else false

  :num_in:Input number to test
  :true or false

  """
  ii=2
  while ii <= sqrt(num_in):
    if num_in % ii ==0:
      return False
    ii+=1

  return True


num = 600851475143
factors = []
ii = 1
while ii <= sqrt(num):
  if num % ii ==0:
    if is_prime(ii):
      factors.append(ii)
    if is_prime(num/ii):
      factors.append(num/ii)
  ii+=1

print'Prime Factors of ',num, ' are: ',sort(factors)
print 'Largest Prime Factor of ',num,' is: ',max(factors)
