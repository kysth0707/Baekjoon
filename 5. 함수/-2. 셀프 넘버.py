# 모름
# https://www.acmicpc.net/problem/4673

def d(n):
	Sum = n
	for i in range(len(str(n))):
		Sum += int(str(n)[i])
	return Sum

a = 1
while True:
	Value = d(a)
	if Value > 20:
		break
	print(Value)
	a += 1