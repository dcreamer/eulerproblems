#!/usr/bin/env python3
import numpy as np
import random

accomplished=[1,3,5,7,9,12,16,20,25,14,34,29,26,27,36,30,32,2,4,6,8,10]
print(len(accomplished))

# Problem 2
def even_fib(n):
	x=1
	y=2
	evens=[2]
	boo=False
	while boo==False:
		z=x+y
		x=y
		y=z
		if z%2==0:
			evens.append(z)
		if z>n:
			break
	print(sum(evens))
#even_fib(4*10**6)

# Problem 4
def largest_palin(n):
#	def palin(x):
#		word=str(x)
#		back=reversed(word)
	maxie=1
	for aa in range(n):
		for bb in range(n):
			num=aa*bb
			palin=str(num)
			if num>maxie and palin==palin[::-1]:
				maxie=num
	print(maxie)
#largest_palin(10**3)

# Problem 6
def sum_sqr_dif(n):
	def sum_sqrs(x):
		blah=[]
		for aa in range(x+1):
			blah.append(aa**2)
		y=sum(blah)
		return y
	def sqr_sums(x):
		blah=[]
		for aa in range(x+1):
			blah.append(aa)
		y=sum(blah)**2
		return y
	z=sqr_sums(n)-sum_sqrs(n)
	print(z)
#sum_sqr_dif(100)

# Problem 8
def max_product(n):
	x=str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
	arr=[]
	maxie=1
	for aa in range(len(x)):
		arr.append(int(x[aa]))
	for aa in range(len(arr)-n):
		x=arr[aa]
		for bb in range(aa,aa+n-1):
			x=x*arr[bb]
		if x>maxie:
			maxie=x
	print(maxie)
#max_product(13)

# Problem 10
def prime_sum(n):
	nums=set(range(2,n))
	for aa in range(2,int(np.sqrt(n))+1):
		for bb in range(2*aa,n,aa):
			nums.discard(bb)
	num=sum(nums)
	print(num)
#prime_sum(2*10**6)

