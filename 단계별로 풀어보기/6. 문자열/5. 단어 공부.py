Alphabets = "abcdefghijklmnopqrstuvwxyz"
Data = input().lower()
Result = []

for i in range(len(Alphabets)):
	Result.append(Data.count(Alphabets[i]))
	
Max = max(Result)
Count = 0
for i in range(len(Result)):
	if Result[i] == Max:
		Count += 1
if Count > 1:
	print("?")
else:
	print(Alphabets[Result.index(Max)].upper())