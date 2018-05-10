#!/usr/bin/env python3
import numpy as np
import random

names=open("names.txt","r")
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums=np.arange(1,27,1)
dic={}
for aa in range(len(nums)):
	dic[alpha[aa]]=nums[aa]

lips=[]
for line in names:
	for word in line.split():
		lips.append(word)
lips.sort()
def name_num(x):
	x=x.lower()
	num=0
	for aa in x:
		num+=dic[aa]
	return num
ans=0
for aa in range(len(lips)):
	score=(aa+1)*name_num(lips[aa])
	ans+=score
print(ans)		
