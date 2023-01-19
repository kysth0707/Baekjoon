a=int(input())
Num = 0
while True:
	if a % 3 == 0:
		a=int(a/3)
	elif a % 2 == 0:
		a=int(a/2)
	else:
		if (a-1) % 3 == 0:
			a-=1
		elif (a-1) % 2 == 0:
			a-=1
		else:
			a-=1

	Num += 1
	if a == 1:
		print(Num)
		break