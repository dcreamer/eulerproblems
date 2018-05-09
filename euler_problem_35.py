#!/usr/bin/env python3
import numpy as np
import random

# Problem 35
def circ_primes(n):
	def prime_test(num):
		num=int(num)
		for kk in range(2,int(np.sqrt(num))+1):
			if num%kk==0:
				return False
		return True

	def rotate(x):
		return [x[n:]+x[:n] for n in range(1,len(x))]

	nums=set(range(2,n))
	for aa in range(2,int(np.sqrt(n))+1):
		for bb in range(2*aa,n,aa):
			nums.discard(bb)
	crumbs=list(nums)

	s=[0,2,4,5,6,8]
	primes=set(['2','5']+[str(p) for p in crumbs if not set(str(p)).intersection(s)])
	x=sum(all(q in primes for q in rotate(p)) for p in primes)
	print(x)
circ_primes(10**6)
