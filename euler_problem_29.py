#!/usr/bin/env python3
import numpy as np
import random

# Problem 29
def distinct_powers():
	liz=[]
	jenna=2
	dotcom=100
	for aa in range(jenna,dotcom+1):
		for bb in range(jenna,dotcom+1):
			liz.append(aa**bb)
	kris=len(list(set(liz)))
	print(kris)
distinct_powers()
