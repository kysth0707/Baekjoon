a=0
b=1
c=int(input())
for i in range(c):
	d=a+b
	a=b
	b=d
print(a)

# 나중에 재귀로 고쳐보자