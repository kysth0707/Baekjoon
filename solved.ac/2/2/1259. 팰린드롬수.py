import sys
while True:
	a=sys.stdin.readline().rstrip()
	if a=="0":
		break
	b=len(a)
	e=True
	for i in range(int(b/2)):
		if a[i] != a[b-1-i]:
			print("no")
			e=False
			break
	if e:
		print("yes")
