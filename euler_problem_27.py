#!/usr/bin/env python3
import numpy as np
import random

# Problem 27
def f(n,a,b):
	return n**2+b*n+a

def prime_test(num):
	num=abs(int(num))
	for kk in range(2,int(np.sqrt(num))+1):
		if num%kk==0:
			return False
	return True

maxie=0
best_a=0
best_b=0
for aa in range(-1000,1000):
	for bb in range(-1001,1001):
		nums=[]
		for cc in range(1000):
			pos_primes=f(cc,aa,bb)
			if prime_test(pos_primes)==True:
				nums.append(pos_primes)
			else:
				break
		length=len(nums)
		if length>maxie:
			maxie=length
			best_a=aa
			best_b=bb
ans=best_a*best_b
print(ans)
