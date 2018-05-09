#!/usr/bin/env python3
import numpy as np
import random

# A. Euler Problem 30: Digit fifth powers
def dig_fifth(d):
	syrup=[]
	for aa in range(0,10000000):
		div=str(aa)
		num=0
		for bb in range(0,len(div)):
			num=num+int(div[bb])**d
		if aa==num:
			syrup.append(aa)
	maple=sum(syrup)-1
	print(maple)
dig_fifth(5)
