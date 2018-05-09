#!/usr/bin/env python3
import numpy as np
import random

# B. Euler Probem 16: Largest Prime Factor
def power_sum():
	num=str(2**1000)
	blah=[]
	for aa in range(0,len(num)):
		blah.append(int(num[aa]))
	ans=sum(blah)
	print(ans)
power_sum()
