import sys, statistics

a=int(input())
b=[int(sys.stdin.readline().rstrip()) for _ in range(a)]
print(round(sum(b)/a))
print(sorted(b)[int((a-1)/2)])
MyDict = {}
for x in b:
	MyDict[x] = 1 if MyDict.get(x) == None else MyDict[x] + 1

MaxCount = -1000
MaxValues = []
for key, value in MyDict.items():
	if MaxCount < value:
		MaxValues = []
		MaxValues.append(key)
		MaxCount = value
	elif MaxCount == value:
		MaxValues.append(key)
MaxValues = sorted(MaxValues)
print(MaxValues[0] if len(MaxValues) == 1 else MaxValues[1])
print(max(b)-min(b))