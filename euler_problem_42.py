#!/usr/bin/env python3
import numpy as np
import random

# Problem 42

def removeQuotes(word):
	return word.replace("\"","")
f=open("words.txt","r")
#for line in f:
#	for word in line.split(","):
#		removeQuotes(word)

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums=np.arange(1,27,1)
dic={}
for aa in range(len(nums)):
	dic[alpha[aa]]=nums[aa]

def t(n):
	return 1/2*n*(n+1)

def name_num(x):
	x=x.lower()
	num=0
	for aa in x:
		num+=dic[aa]
	return num

trigs=[]
for aa in range(0,100):
	trigs.append(t(aa))

triangle_words=0
for line in f:
	for word in line.split(","):
		x=name_num(removeQuotes(word))
		if x in trigs:
			triangle_words+=1
print(triangle_words)
