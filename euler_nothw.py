#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
import numpy.linalg as la
import random as rand

# A. Euler Problem 26: Reciprocal Cycles
def rem_cyc(d):
	dic_num={}
	fin_num={}

	for aa in range(1,d):
		num=1
		for bb in range(1,d):
			num=(10*num)%aa
			if num==1:
				dic_num[aa]=bb
				break
	fin_num=sorted(dic_num.items(),key=lambda x: x[1])
	print(fin_num)
#rem_cyc(1000)
#		boo=False
#		while boo==False:
#			n=n+1
#			num=(num*10)%aa
#			arr.append(num)
#			if arr[n-1]==arr[0] and len(arr)>lens:
#				lens=len(arr)
#				maxie=int(aa)
#				boo==True
#				break
#				print(maxie)
#			break
#rem_cyc(10)

# B. Euler Problem 27: Quadratic Primes
def quad_primes():
	def f(n):
		return n**2+a*n+b
#quad_primes()
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
#doub_pal(10**6)

# II. Euler Problem 39: Integer Right Triangles
def right_trigs(f):
	maxie=0
	lens=0
	for cc in range(1,f):
		for bb in range(0,cc):
			num=[]
			b=cc*(2*bb-cc)/(2*(bb-cc))
			c=np.sqrt(bb**2+b**2)
			num.append(bb)
			if isinstance(b,int)==True:
				num.append(b)
			if isinstance(c,int)==True:
				num.append(c)
			if len(num)>lens:
				lens=len(num)
				maxie=int(cc)
	print(lens)
#right_trigs(1000)

# A. Euler Problem 30: Digit fifth powers
def dig_fifth(d):
	syrup=[]
	for aa in range(0,10000000):
		div=str(aa)
		num=0
		for bb in range(0,len(div)):
			num=num+int(div[bb])**d
		if aa==num:
			syrup.append(aa)
	maple=sum(syrup)-1
	print(maple)
#dig_fifth(5)

# B. Euler Problem 32: Pandigital products
def lis_check(f):
	for cc in range(0,len(f)):
		binary_solo=[]
		for dd in range(cc,len(f)-1):
			if f[cc]!=f[dd+1]:
				binary_solo.append(0)
			if f[cc]==f[dd+1] or f[cc]==0:
				binary_solo.append(1)
		if binary_solo.count(1)>=1:
			return False
	return True
def pan_prod():
	prods=[]
	for ff in range(0,2000):
		for gg in range(0,2000):
			h=ff*gg
			n=str(h)+str(ff)+str(gg)
			hoffa=[int(y) for y in n]
			if lis_check(hoffa)==True and len(hoffa)==9 and prods.count(h)==0:
				prods.append(h)
	print(sum(prods))
#pan_prod()
