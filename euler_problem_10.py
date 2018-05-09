#!/usr/bin/env python3
import numpy as np
import random

# Problem 10
def prime_sum(n):
	nums=set(range(2,n))
	for aa in range(2,int(np.sqrt(n))+1):
		for bb in range(2*aa,n,aa):
			nums.discard(bb)
	num=sum(nums)
	print(num)
prime_sum(2*10**6)
