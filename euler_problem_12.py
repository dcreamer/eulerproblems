#!/usr/bin/env python3
import numpy as np
import random

# Problem 12.
def high_div_trig():
	boo=False
	n=0
	while boo==False:
		trig_num=0
		facts=[]
		n=n+1
		n0=np.arange(0,n+1)
		trig_num=sum(n0)
		for aa in range(1,int(np.sqrt(trig_num))):
			if trig_num%aa==0:
				facts.append(aa)
				facts.append(trig_num/aa)
			num=len(facts)
			if num>500:
				boo=True
				print(trig_num)
				break
high_div_trig()

