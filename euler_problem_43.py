#!/usr/bin/env python3
import numpy as np
import random
from itertools import permutations

# Problem 43

primes=[2,3,5,7,11,13,17]
digits=[9,8,7,6,5,4,3,2,1,0]

def sub_string(num,index):
	index-=1
	return int(str(num)[index:index+3])
def killer_of_lists(x):
	num=0
	for i in range(len(x)):
		num+=x[i]*10**(len(x)-i-1)
	return num

def fits_def(num):
	for i in range(2,9):
		if sub_string(num,i)%primes[i-2]:
			return False
	return True

total=0
for lice in permutations(digits):
	if fits_def(killer_of_lists(lice)):
		total+=killer_of_lists(lice)
print(total)
