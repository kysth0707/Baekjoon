a,b=map(int,input().split())
c=[i+1 for i in range(a)]
d=-1
e=[]
while True:
	if len(c)==0:
		break
	d+=b
	d%=len(c)
	e.append(str(c.pop(d)))
	d-=1
print(f'<{", ".join(e)}>')