#!/usr/bin/env python3
import scipy as sp
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import random
from random import randint


# Euler Problem 1: Multiples of 3 and 5
def mult_3and5():
	numA=1000
	ansA=0
	for aa in range(0,numA):
		if float(aa%3)==0 or float(aa%5)==0:
			ansA=ansA+aa
	print(ansA)
#mult_3and5()

# Euler Problem 3: Largest prime factor
def prime_test(num):
	num=int(num)
	for kk in range(2,int(np.sqrt(num))+1):
		if num%kk==0:
			return False
	return True

def largest_prime():
#	numB=600851475143
#	factsB=[]
#	for bb in range(1,numB+1):
#		if numB%bb==0 and prime_test(bb)==True:
#			factsB.append(bb)
#	print(max(factsB))
	num=600851475143
	arr=[]
	for kk in range(2,int(np.sqrt(num))++1):
		if  num%kk==0 and prime_test(kk)==True:
			arr.append(kk)
	print("The largest prime factor: ",arr[-1])
#largest_prime()
# This solution was produced with the in class help of Gavril Schedrin and the commented portion represents a failed solo attempt which I was unable to torubleshoot.

# C. Euler Problem 5: Smallest Multiple
def smallest_mult():
	num=0
	boo=False
	rangC=np.arange(2,20,1)
	while boo!=True:
		num=num+20
		boo=True
		for ee in range(0,len(rangC)):
			if num%rangC[ee]!=0:
				boo=False
				break
		if boo:
			break
	print(num)
#smallest_mult()

# D. Euler Problem 7: 10001st Prime
def sub_prime():
	num=1
	num0=0
	while True:
		num=num+1
		if prime_test(num):
			num0=num0+1
		if num0==10001:
			print(num)
			break
#sub_prime()

# E. Euler Problem 9: Special Pythagorean triplet
def pythag():
	for aa in range(1,202):
		b=int((2000*aa-1000**2)/(2*aa-2000))
		c=int(np.sqrt(aa**2+b**2))
		if aa+b+c==1000:
			print(aa*b*c)
pythag()

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
#high_div_trig()

# A. Euler Problem 11: Largest product in a grid
def grid():
	arr=np.zeros((20,20), dtype='int')
	etta=[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8,49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0,81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65,52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91,22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50,32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21,24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95,78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92,16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57,86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58,19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40,4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66,88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69,4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36,20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16,20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54,1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]
	for aa in range(0,20):
		for bb in range(0,20):
			arr[aa][bb]=etta[20*aa+bb]
	step=4
	for ff in range(0,20):
		for cc in range(0,20-step):
			etta_max_row=1
			etta_max_col=1
			etta_max_rdiag1=1
			etta_max_rdiag2=1
			etta_max_ldiag1=1
			etta_max_ldiag2=1
			row_most=1
			col_most=1
			rdiag_most=1
			ldiag_most=1
			for ee in range(0,step):
				etta_max_row=etta_max_row*arr[ff][cc+ee]
				etta_max_col=etta_max_col*arr[cc+ee][ff]
			if etta_max_row>row_most:
				row_most=etta_max_row
			if etta_max_col>col_most:
				col_most=etta_max_col
	for gg in range(0,20-step):
		for hh in range(0,20-step):
			for ii in range(0,step):
				etta_max_rdiag1=etta_max_rdiag1*arr[gg+ii][gg+ii]
				etta_max_ldiag=etta_max_ldiag*arr[19-gg-ii][hh+ii]
			if etta_max_rdiag>rdiag_most:
				rdiag_most=etta_max_rdiag
			if etta_max_ldiag>ldiag_most:
				ldiag_most=etta_max_ldiag	
	print(col_most,row_most,rdiag_most,ldiag_most)
#grid()

# B. Euler Probem 16: Largest Prime Factor
def power_sum():
	num=str(2**1000)
	blah=[]
	for aa in range(0,len(num)):
		blah.append(int(num[aa]))
	ans=sum(blah)
	print(ans)
#power_sum()

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
#fact_sum()

# D. Euler Problem 25: 1000 Digit Fibonacci
def fib_num():
	n=1
	f1=[1,1]
	fib=False
	while fib!=True:
		n=n+1
		fib=False
		f1.append(f1[n-1]+f1[n-2])
		if len(str(f1[n]))==1000:
			fib=True
			break
	for i in [i for i, x in enumerate(f1) if x==1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816
]:
		print(i+1)
fib_num()
# Problem 14
def collatz():
	def f(x):
		if x%2==0:
			return x/2
		if x%2!=0:
			return 3*x+1
	maxie=0
	n=1
	for aa in range(10**5,10**6):
		start=aa
		boo=False
		lis=[]
		while boo==False:
			start=f(start)
			lis.append(start)
			if start==1:
				break
		lens=len(lis)
		if lens>n:
			n=lens
			maxie=aa
	print(maxie)
#collatz()

# Problem 34
def digit_factorials():
	def factorial(x):
		michael=1
		job=np.arange(1,x+1,1)
		for dd in range(len(job)):
			michael=michael*job[dd]
		return michael

	p=[]
	for aa in range(3,10**5):
		bluth=str(aa)
		buster=[]
		n=0
		for bb in range(0,len(bluth)):
			buster.append(int(bluth[bb]))
		for cc in range(len(buster)):
			n=n+factorial(buster[cc])
		if n==aa:
			p.append(aa)
	print(sum(p))
#digit_factorials()

# Problem 29
def distinct_powers():
	liz=[]
	jenna=2
	dotcom=100
	for aa in range(jenna,dotcom+1):
		for bb in range(jenna,dotcom+1):
			liz.append(aa**bb)
	kris=len(list(set(liz)))
	print(kris)
#distinct_powers()
