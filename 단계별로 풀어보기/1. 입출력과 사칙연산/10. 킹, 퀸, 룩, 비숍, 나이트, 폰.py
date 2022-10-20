Having = list(map(int, input().split(' ')))
Target = [1, 1, 2, 2, 2, 8]
for i in range(6):
	print(Target[i] - Having[i],end=' ')