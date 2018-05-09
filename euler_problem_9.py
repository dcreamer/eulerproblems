#!/usr/bin/env python3
import numpy as np
import random

# E. Euler Problem 9: Special Pythagorean triplet
def pythag():
	for aa in range(1,202):
		b=int((2000*aa-1000**2)/(2*aa-2000))
		c=int(np.sqrt(aa**2+b**2))
		if aa+b+c==1000:
			print(aa*b*c)
pythag()
