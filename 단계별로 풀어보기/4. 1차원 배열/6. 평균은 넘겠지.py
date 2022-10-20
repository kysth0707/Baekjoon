Length = int(input())
for i in range(Length):
	Data = list(map(int, input().split(' ')))
	del Data[0]
	Average = sum(Data) / len(Data)

	Sum = 0
	for x in Data:
		if x > Average:
			Sum += 1
	try:
		print("{:.3f}%".format(Sum / len(Data) * 100))
	except:
		print("0.000%")