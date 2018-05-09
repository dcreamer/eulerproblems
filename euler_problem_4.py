#!/usr/bin/env python3
import numpy as np
import random

# Problem 4
def largest_palin(n):
	maxie=1
	for aa in range(n):
		for bb in range(n):
			num=aa*bb
			palin=str(num)
			if num>maxie and palin==palin[::-1]:
				maxie=num
	print(maxie)
largest_palin(10**3)
