#!/usr/bin/env python3
import numpy as np
import random

# Problem 21
def amicable_numbers(n):
	def factors(x):
		blah=[]
		for aa in range(1,int(x/2)+1):
			if x%aa==0:
				blah.append(aa)
		return sum(blah)
	blah=[]
	for aa in range(0,n):
		y=aa
		x=factors(y)
		if y==factors(x) and x!=y:
			blah.append(y)
	print(sum(blah))
amicable_numbers(10000)
