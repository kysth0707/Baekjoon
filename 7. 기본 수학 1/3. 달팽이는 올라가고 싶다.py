Day, Night, Target = list(map(int, input().split(' ')))

Height = 0
Count = 0

Count = (Target - Night) // (Day - Night)
if (Target - Night) % (Day - Night) != 0:
	print(Count + 1)
else:
	print(Count)


# 우선 풀기는 했는데
# 아래 거 보고 충격받았다
# 어떻게 저걸 생각해내지? ㄷㄷ
# https://www.acmicpc.net/board/view/96187


# 너무 느림
# while True:
# 	Height += Day
# 	Count += 1
# 	if Height >= Target:
# 		break
# 	Height -= Night
# print(Count)