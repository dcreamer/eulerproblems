#!/usr/bin/env python3
import numpy as np
import random

# Problem 34
def digit_factorials():
	def factorial(x):
		michael=1
		job=np.arange(1,x+1,1)
		for dd in range(len(job)):
			michael=michael*job[dd]
		return michael

	p=[]
	for aa in range(3,10**5):
		bluth=str(aa)
		buster=[]
		n=0
		for bb in range(0,len(bluth)):
			buster.append(int(bluth[bb]))
		for cc in range(len(buster)):
			n=n+factorial(buster[cc])
		if n==aa:
			p.append(aa)
	print(sum(p))
digit_factorials()
