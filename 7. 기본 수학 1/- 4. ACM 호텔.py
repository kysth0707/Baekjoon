# 왜 안되지?
# https://www.acmicpc.net/problem/10250

Length = int(input())
for i in range(Length):
	h, w, m = list(map(int, input().split(' ')))
	Height = m % h
	Width = m//h + 1
	print(f"{(Height)}{str(Width).zfill(2)}")