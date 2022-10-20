Length = int(input())
Count = 0
for i in range(Length):
	Data = input()
	Sum = []
	Now = Data[0]
	No = False
	for x in range(len(Data)):
		if Data[x] in Sum and Now != Data[x]:
			No = True
			break
		Sum += Data[x]
		Now = Data[x]
	if not No:
		Count += 1
print(Count)