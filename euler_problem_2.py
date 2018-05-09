#!/usr/bin/env python3
import numpy as np
import random

# Problem 2
def even_fib(n):
	x=1
	y=2
	evens=[2]
	boo=False
	while boo==False:
		z=x+y
		x=y
		y=z
		if z%2==0:
			evens.append(z)
		if z>n:
			break
	print(sum(evens))
even_fib(4*10**6)
