import sys
a=int(input())
b=[sys.stdin.readline().rstrip().split(' ') for i in range(a)]
b.sort(key=lambda x:int(x[0]))
for i in range(a):
	print(f"{b[i][0]} {b[i][1]}")