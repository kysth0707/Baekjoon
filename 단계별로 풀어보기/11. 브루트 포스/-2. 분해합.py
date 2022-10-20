import sys
sys.setrecursionlimit(10**6)

def Get(x):
	Sum=x
	for data in str(x):
		Sum+=int(data)
	return Sum

target=int(input())
for i in range(10, target):
	if Get(i)==target:
		print(i)
		break