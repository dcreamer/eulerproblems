#!/usr/bin/env python3
import numpy as np
import random

# 1. Euler Problem 36: Double_Base Palindrome
def doub_pal(d):
	nums=np.arange(0,d,1)
	palins=[]
	for aa in range(0,len(nums)):
		dig=str(nums[aa])
		binary=str(bin(nums[aa]))+"b"+"0"
		if dig==dig[::-1] and binary==binary[::-1] and binary[0]!=0:
			palins.append(aa)
	print(sum(palins))
doub_pal(10**6)
