Best = 0
BestNum = 0
for i in range(9):
	val = int(input())
	if val > Best:
		Best = val
		BestNum = i
print(Best)
print(BestNum + 1)