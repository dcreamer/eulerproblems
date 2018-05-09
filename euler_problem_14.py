#!/usr/bin/env python3
import numpy as np
import random

# Problem 14
def collatz():
	def f(x):
		if x%2==0:
			return x/2
		if x%2!=0:
			return 3*x+1
	maxie=0
	n=1
	for aa in range(10**5,10**6):
		start=aa
		boo=False
		lis=[]
		while boo==False:
			start=f(start)
			lis.append(start)
			if start==1:
				break
		lens=len(lis)
		if lens>n:
			n=lens
			maxie=aa
	print(maxie)
collatz()
