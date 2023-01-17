def BunhaeHap(Value):
	ReturnValue = Value
	for x in str(Value):
		ReturnValue += int(x)
	return ReturnValue

TargetNum = int(input())
LowestValue = -1
for num in range(TargetNum, 0, -1):
	if BunhaeHap(num) == TargetNum:
		LowestValue = num
print(0 if LowestValue == -1 else LowestValue)