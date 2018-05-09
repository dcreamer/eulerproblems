#!/usr/bin/env python3
import numpy as np
import random

# Problem 23
def unundant_sums(n):
	def factors(x):
		blah=[]
		for aa in range(1,int(x/2)+1):
			if x%aa==0:
				blah.append(aa)
		return sum(blah)
	abundant=[]
	for aa in range(0,n+1):
		if factors(aa)>aa:
			abundant.append(aa)
	print(abundant)
	nums=set(range(1,n))
	for aa in range(len(abundant)):
		for bb in range(len(abundant)):
			sums=abundant[aa]+abundant[bb]
			nums.discard(sums)
	print(sum(nums))
unundant_sums(28124)

