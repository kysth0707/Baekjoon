# 실패
# 
import sys

Length = int(input())
Values = []
for i in range(Length):
	Values.append(int(sys.stdin.readline()))


Max = max(Values)
new = []
new2 = []
for i in range(Max):
	new.append([])

for i in Values:
	new[i - 1].append(i)

for i in new:
	if i != []:
		new2.append(i[0])

print('\n'.join(str(s) for s in new2))