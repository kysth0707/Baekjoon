def IsD(a):
	if a < 2:
		return False
	i = 1
	while True:
		i += 1
		if i >= a:
			return True
		if a % i == 0:
			return False
MinVal = int(input())
MaxVal = int(input())

Hap = 0
Min = -1
for Num in range(MinVal, MaxVal + 1):
	if IsD(Num):
		if Min == -1:
			Min = Num
		Hap += Num
if Min == -1:
	print(-1)
else:
	print(Hap)
	print(Min)