#!/usr/bin/env python3
import numpy as np
import random

# Problem 39
def pythag(a,b):
	return (a**2+b**2)**(1/2)

def solutions(p):
	temp=0
	for aa in range(1,int(p/2)):
		for bb in range(aa,int(p/2)):
			if aa+bb+pythag(aa,bb)==p:
				temp+=1
	return temp


maxie=0
for aa in range(1,1001):
	if solutions(aa)>maxie:
		maxie=solutions(aa)
		ans=aa
print(ans)
