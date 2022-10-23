import sys
a=int(input())
for i in range(a):
	h,w,n=map(int,sys.stdin.readline().rstrip().split(' '))
	n-=1
	print(f"{n%h+1}{str(n//h+1).zfill(2)}")