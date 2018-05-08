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

# Problem 37
def truncatable_primes():
	for aa in range(10,4000):
		if aa%2==0:
			break
		if aa%2!=0:
			jeff=str(aa)
				for bb in range(len(jeff)):
				
truncatable_primes()
