#!/usr/bin/env python3
import numpy as np
import random

accomplished=[1,3,5,7,9,12,16,20,25,14,34,29,26,27,36,30,32,2,4,6,8,11,15,21]
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

# Problem 11
def max_prod():
	L = []
	L.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
	L.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
	L.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
	L.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
	L.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
	L.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
	L.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
	L.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
	L.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
	L.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
	L.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
	L.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
	L.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
	L.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
	L.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
	L.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
	L.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
	L.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
	L.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
	L.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")	

	mat=[aa.split() for aa in L]
	mat=[[int(bb) for bb in aa] for aa in mat]

	maxie=0
	for aa in range(20):
		for bb in range(16):
			prod=mat[aa][bb]*mat[aa][bb+1]*mat[aa][bb+2]*mat[aa][bb+3]
			if prod>maxie:
				maxie=prod
			prod=mat[bb][aa]*mat[bb+1][aa]*mat[bb+2][aa]*mat[bb+3][aa]
			if prod>maxie:
				maxie=prod
	for aa in range(16):
		for bb in range(16):
			prod=mat[aa][bb]*mat[aa+1][bb+1]*mat[aa+2][bb+2]*mat[aa+3][bb+3]
			if prod>maxie:
				maxie=prod
	for aa in range(3,20):
		for bb in range(16):
			prod=mat[aa][bb]*mat[aa-1][bb+1]*mat[aa-2][bb+2]*mat[aa-3][bb+3]
			if prod>maxie:
				maxie=prod
	print(maxie)
#max_prod()

# Problem 15
def lattice_paths(n):
	dl=[1]*n
	for aa in range(n):
		for bb in range(aa):
			dl[bb]=dl[bb]+dl[bb-1]
		dl[aa]=2*dl[aa-1]
	print(dl[n-1])		
#lattice_paths(20)

# Problem 21
def amicable_numbers(n):
	def factors(x):
		blah=[]
		for aa in range(1,int(x/2)+1):
			if x%aa==0:
				blah.append(aa)
		return sum(blah)
	blah=[]
	for aa in range(0,n):
		y=aa
		x=factors(y)
		if y==factors(x) and x!=y:
			blah.append(y)
	print(sum(blah))
#amicable_numbers(10000)

# Problem 35
def circ_primes(n):
	def rotate(x):
		return x[1:]+x[:1]
	nums=set(range(2,n))
	for aa in range(2,int(np.sqrt(n))+1):
		for bb in range(2*aa,n,aa):
			nums.discard(bb)
	crumbs=list(nums)
	x=[]
	for aa in range(len(crumbs)):
		word=str(crumbs[aa])
		x.append(int(rotate(word)))
	
circ_primes(100)
