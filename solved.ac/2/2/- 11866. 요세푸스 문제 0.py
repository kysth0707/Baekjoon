a,b=map(int,input().split())
b-=1
c=[i for i in range(1, a+1)]
d=0
while True:
	if len(c)==0:
		break
	d=(d + b)%len(c)
	print(c[d])
	del c[d]