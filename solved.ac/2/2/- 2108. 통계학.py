# https://www.acmicpc.net/problem/2108
import sys
a=int(input())
b=[]
for i in range(a):
	b.append(int(sys.stdin.readline().rstrip()))
print(int(sum(b)/a))
print(sorted(b)[int(a/2)])
# 최빈값 고치기
print(max(b)-min(b))