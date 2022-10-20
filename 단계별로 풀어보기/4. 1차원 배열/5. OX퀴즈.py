Length = int(input())
for i in range(Length):
	Value = str(input())
	Stack = 0
	Score = 0
	for x in range(len(Value)):
		if Value[x] == "O":
			Stack += 1
			Score += Stack
		else:
			Stack = 0
	print(Score)