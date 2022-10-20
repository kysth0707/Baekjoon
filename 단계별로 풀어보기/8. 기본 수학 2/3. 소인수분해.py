Num = int(input())
No = False
Last = 2
while True:
	d = Last
	while True:
		if Num % d == 0:
			Num = Num // d
			Last = d
			print(d)
			break
		d += 1
		if d > Num:
			No = True
			break
	if No:
		break
if Num != 1:
	print(Num)