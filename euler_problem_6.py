#!/usr/bin/env python3
import numpy as np
import random

# Problem 6
def sum_sqr_dif(n):
	def sum_sqrs(x):
		blah=[]
		for aa in range(x+1):
			blah.append(aa**2)
		y=sum(blah)
		return y
	def sqr_sums(x):
		blah=[]
		for aa in range(x+1):
			blah.append(aa)
		y=sum(blah)**2
		return y
	z=sqr_sums(n)-sum_sqrs(n)
	print(z)
sum_sqr_dif(100)
