import sys
a=int(input())
b=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(a)]
b.sort(key=lambda x:(x[0], x[1]))
for i in range(a):
	print(f"{b[i][0]} {b[i][1]}")