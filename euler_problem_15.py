#!/usr/bin/env python3
import numpy as np
import random

# Problem 15
def lattice_paths(n):
	dl=[1]*n
	for aa in range(n):
		for bb in range(aa):
			dl[bb]=dl[bb]+dl[bb-1]
		dl[aa]=2*dl[aa-1]
	print(dl[n-1])		
lattice_paths(20)
