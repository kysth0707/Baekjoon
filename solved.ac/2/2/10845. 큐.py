import sys
a=int(input())
b=[]
for i in range(a):
	c=sys.stdin.readline().rstrip().split(' ')
	d=c[0]
	if d=="push":
		b.append(c[1])
	elif d=="pop":
		print(-1 if len(b)==0 else b.pop(0))
	elif d=="size":
		print(len(b))
	elif d=="empty":
		print(1 if len(b)==0 else 0)
	elif d=="front":
		print(-1 if len(b)==0 else b[0])
	elif d=="back":
		print(-1 if len(b)==0 else b[-1])