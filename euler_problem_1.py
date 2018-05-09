#!/usr/bin/env python3
import numpy as np
import random

# Euler Problem 1: Multiples of 3 and 5
def mult_3and5():
	numA=1000
	ansA=0
	for aa in range(0,numA):
		if float(aa%3)==0 or float(aa%5)==0:
			ansA=ansA+aa
	print(ansA)
mult_3and5()
