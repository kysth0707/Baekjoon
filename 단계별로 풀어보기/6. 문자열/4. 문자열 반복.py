Length = int(input())
for i in range(Length):
	Values = input().split(' ')
	Result = ""
	for x in range(len(Values[1])):
		Result += Values[1][x] * int(Values[0])
	print(Result)