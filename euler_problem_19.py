#!/usr/bin/env python3
import numpy as np
import random

# Problem 19
days=365
months=[31,28,31,30,31,30,31,31,30,31,30,31]
year=1901
first_sunday=7
num_suns=0
for aa in range(1901,2001):
	for bb in range(len(months)):
		if bb==1 and not aa%4 and aa%100:
			first_sunday+=29
		else:
			first_sunday+=months[bb]
		if not first_sunday%7:
			first_sunday=0
			num_suns+=1
print(num_suns)
