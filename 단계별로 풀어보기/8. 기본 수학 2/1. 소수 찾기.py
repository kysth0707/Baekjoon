input()
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
Nums = list(map(int, input().split(' ')))
Count = 0
for Num in Nums:
	if IsD(Num):
		Count += 1
print(Count)