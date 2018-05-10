#!/usr/bin/env python3
import numpy as np
import random

# Problem 67
def max_path_sum():
	rows=0
	numbers=[]
	f=open("p067_triangle.txt")
	for line in f:
		rows+=1
		for word in line.split():
			numbers.append(int(word))

	nothings=np.zeros((100,100))
	triangle=np.zeros((100,100))
	index=0
	for i in range(rows):
		for j in range(i+1):
			triangle[i][j]=numbers[index]
			index+=1	
	nothings[len(triangle)-1]=triangle[len(triangle)-1]

	def f(i,j):
		if i==99 or nothings[i][j]>0:
			return nothings[i][j]
		nothings[i][j]=triangle[i][j]+max(f(i+1,j),f(i+1,j+1))
		return nothings[i][j]
	f(0,0)
	print(nothings[0][0])		
max_path_sum()
