#!/usr/bin/env python3
import numpy as np
import random

# Problem 28 
def num_spiral(n):
	nums=[1]
	x=1
	spirals=n-2
	for aa in range(1,spirals):
		for bb in range(0,4):
			x=x+(2)*aa
			nums.append(x)
		if x>spirals**2:
			break
	print(sum(nums))
num_spiral(1001)
