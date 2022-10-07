Alphabets = "abcdefghijklmnopqrstuvwxyz"
Data = input()
Values = []
for i in range(len(Alphabets)):
	Values.append(str(Data.find(Alphabets[i])))
print(" ".join(Values))