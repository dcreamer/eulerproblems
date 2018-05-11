#!/usr/bin/env python3
import numpy as np
import random
from itertools import permutations

# Problem 41

def prime_test(x):
	for aa in range(2,int(np.sqrt(x)+1)):
		if x%aa==0:
			return False
	return True

def killer_of_lists(x):
	num=0
	for i in range(len(x)):
		num+=x[i]*10**(len(x)-i-1)
	return num
pols=[7,6,5,4,3,2,1]
killer_of_lists(pols)
for lice in permutations(pols):
	if prime_test(killer_of_lists(lice)):
		print(killer_of_lists(lice))
		break
	
