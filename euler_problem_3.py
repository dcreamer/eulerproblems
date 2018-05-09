#!/usr/bin/env python3
import numpy as np
import random

# Euler Problem 3: Largest prime factor
def prime_test(num):
	num=int(num)
	for kk in range(2,int(np.sqrt(num))+1):
		if num%kk==0:
			return False
	return True

def largest_prime():
	arr=[]
	for kk in range(2,int(np.sqrt(num))++1):
		if  num%kk==0 and prime_test(kk)==True:
			arr.append(kk)
	print("The largest prime factor: ",arr[-1])
largest_prime()
