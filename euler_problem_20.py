#!/usr/bin/env python3
import numpy as np
import random

# C. Euler Problem 20: Factorial Digit Sum
def fact_sum():
	num=100
	a=num
	for zz in range(1,num):
		a=a*(num-zz)
	b=str(a)
	abed=[]
	for yy in range(0,len(b)):
		abed.append(int(b[yy]))
	brit=sum(abed)
	print(brit)
fact_sum()
