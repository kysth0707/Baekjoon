# 상상력 발휘 실패
# https://www.acmicpc.net/problem/1193

Bunja = 0
Bunmo = 0
Num = int(input())

BunjaUp = True
BunmoUp = True
for i in range(Num):
	if (i - 1) % 4 == 0:
		# 분자 변환
		pass
	if BunjaUp:
		Bunja += 1
	else:
		Bunja -= 1
	
	if BunmoUp:
		Bunmo += 1
	else:
		Bunmo -= 1


# 1, 12321, 123454321
# 1, 5, 9


# += 4

# 121, 1234321, 12345654321
# 3, 7, 11
# += 4