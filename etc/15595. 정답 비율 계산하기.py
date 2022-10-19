# https://www.acmicpc.net/problem/15595
import sys
input = sys.stdin.readline
length = int(input())
Full=0
Suc=0
for i in range(length):
	a=list(input().split(' '))
	if a[1] == "megalusion":
		continue
	Full+=1
	if a[2] == "4":
		Suc+=1
try:
	print(Suc/Full*100)
except:
	print(0)