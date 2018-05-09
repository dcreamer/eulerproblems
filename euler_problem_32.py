#!/usr/bin/env python3
import numpy as np
import random

# B. Euler Problem 32: Pandigital products
def lis_check(f):
	for cc in range(0,len(f)):
		binary_solo=[]
		for dd in range(cc,len(f)-1):
			if f[cc]!=f[dd+1]:
				binary_solo.append(0)
			if f[cc]==f[dd+1] or f[cc]==0:
				binary_solo.append(1)
		if binary_solo.count(1)>=1:
			return False
	return True
def pan_prod():
	prods=[]
	for ff in range(0,2000):
		for gg in range(0,2000):
			h=ff*gg
			n=str(h)+str(ff)+str(gg)
			hoffa=[int(y) for y in n]
			if lis_check(hoffa)==True and len(hoffa)==9 and prods.count(h)==0:
				prods.append(h)
	print(sum(prods))
pan_prod()
