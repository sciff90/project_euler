#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 gareth <gareth@GDS-Desktop>
#
# Distributed under terms of the MIT license.

"""
Project Euler
Problem 9
Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from numpy import *

def gen_tree(A,B,C,D,depth,triplets):
  if depth==1:
    triplets.append(tuple(D))
    triplets.append(tuple(dot(A,D)))
    triplets.append(tuple(dot(B,D)))
    triplets.append(tuple(dot(C,D)))
  else:
    depth=depth-1
    triplets.append(tuple(D))
    gen_tree(A,B,C,dot(A,D),depth,triplets)
    gen_tree(A,B,C,dot(B,D),depth,triplets)
    gen_tree(A,B,C,dot(C,D),depth,triplets)

def sum_nested(list_in):
  list_out = []
  for ii in list_in:
    list_out.append(sum(ii))
  return list_out

A = [[1,-2,2],[2,-1,2],[2,-2,3]]
B = [[1,2,2],[2,1,2],[2,2,3]]
C = [[-1,2,2],[-2,1,2],[-2,2,3]]

D = [3,4,5]

num = 1000
triplets = []
depth =10
gen_tree(A,B,C,D,depth,triplets)

sum_trips = sum_nested(triplets)
print sort(sum_trips)

for ii in sum_trips:
  if 1000 % ii ==0:
    print ii


