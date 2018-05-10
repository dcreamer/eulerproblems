#!/usr/bin/env python3
import numpy as np
import random

# Problem 33
for i in range(1,9):
	for j in range(i+1,10):
		for k in range(1,10):
			if (i*10+k)/(j*10+k)==i/j:
				print((i*10+k)/(j*10+k))
			if (i+k*10)/(j*10+k)==i/j:
				print(i+k*10,j*10+k)
			if (i*10+k)/(j+k*10)==i/j:
				print(i*10+k,j+k*10)
			if (i+k*10)/(j+k*10)==i/j:
				print(i+k*10,j+k*10)
ans=16/64*19/95*26/65*49/98
print(ans)
