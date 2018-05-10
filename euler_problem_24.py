#!/usr/bin/env python3
import numpy as np
import random
from itertools import permutations

# Problem 24
digits=[0,1,2,3,4,5,6,7,8,9]
temp_var=0
for lice in permutations(digits):
	temp_var+=1
	if temp_var==10**6:
		print(lice)
		break
