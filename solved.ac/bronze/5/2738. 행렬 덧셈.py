Height, Width = list(map(int, input().split(' ')))
HangA = [list(map(int, input().split(' '))) for _ in range(Height)]
HangB = [list(map(int, input().split(' '))) for _ in range(Height)]
for y in range(Height):
	for x in range(Width):
		HangA[y][x] += HangB[y][x]
	print(" ".join(map(str, HangA[y])))