#!/usr/bin/env python3
import numpy as np
import random

# Problem 40
num=1
jabba=('1')
lens=0
while lens<=10**6:
	num+=1
	jabba+=str(num)
	lens=len(jabba)

print(int(jabba[0])*int(jabba[9])*int(jabba[99])*int(jabba[999])*int(jabba[9999])*int(jabba[99999])*int(jabba[999999]))

