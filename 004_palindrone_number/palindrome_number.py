#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project Euler problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(num_in):
  """Returns True/False if number is palindrome

  :num_in: @todo
  :returns: @todo

  """
  if str(num_in) == str(num_in)[::-1]:
    return True

  return False

max_val = 0
for ii in range(1,999):
  for jj in range(1,999):
    if is_palindrome(ii*jj) and ii*jj > max_val:
      max_val = ii*jj

print 'Largest Palindrone: ',max_val


