#!/usr/bin/env python3
import numpy as np
import random

def pandigital_check(x):
	jabba=str(x)
	digits=['1','2','3','4','5','6','7','8','9']
	for aa in range(len(digits)):
		if digits[aa] not in jabba:
			return False
	return True

def prod(x):
	jabba=str()
	temp=1
	while len(jabba)<9:
		jabba+=str(x*temp)
		temp+=1
	if len(jabba)>9:
		return 0
	else:
		return int(jabba)
maxie=0
for aa in range(10**5):
	if pandigital_check(prod(aa))==True and prod(aa)>maxie:
		maxie=prod(aa)
print(maxie)
