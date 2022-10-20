a=int(input())
b=int(input())
Sum=0
for i in range(b):
	c,d=map(int, input().split(' '))
	Sum += c * d
print("Yes" if a == Sum else "No")