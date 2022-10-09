Length = int(input())
Values = []
for i in range(Length):
	Values.append(int(input()))
Values = sorted(Values)
print('\n'.join(str(s) for s in Values))