Nums = list(map(int, input().split(' ')))
for i in range(2):
	Nums[i] = int(str(Nums[i])[::-1])
if Nums[0] > Nums[1]:
	print(Nums[0])
else:
	print(Nums[1])