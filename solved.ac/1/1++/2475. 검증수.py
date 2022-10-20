import sys
x=list(map(int, input().split(' ')))
Sum=0
for a in x:
	Sum+=a*a
print(Sum%10)