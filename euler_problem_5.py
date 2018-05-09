#!/usr/bin/env python3
import numpy as np
import random

# C. Euler Problem 5: Smallest Multiple
def smallest_mult():
	num=0
	boo=False
	rangC=np.arange(2,20,1)
	while boo!=True:
		num=num+20
		boo=True
		for ee in range(0,len(rangC)):
			if num%rangC[ee]!=0:
				boo=False
				break
		if boo:
			break
	print(num)
smallest_mult()
