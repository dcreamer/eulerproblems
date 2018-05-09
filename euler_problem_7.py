#!/usr/bin/env python3
import numpy as np
import random

# D. Euler Problem 7: 10001st Prime
def sub_prime():
	num=1
	num0=0
	while True:
		num=num+1
		if prime_test(num):
			num0=num0+1
		if num0==10001:
			print(num)
			break
sub_prime()
