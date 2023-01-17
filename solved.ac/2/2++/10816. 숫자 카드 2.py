CardCount = int(input())
CardList = list(map(int, input().split(' ')))
CardDict = {}
for x in CardList:
	if CardDict.get(x) == None:
		CardDict[x] = 1
	else:
		CardDict[x] += 1
SearchCount = int(input())
SearchList = list(map(int, input().split(' ')))
Output = []
for x in SearchList:
	Output.append("0" if CardDict.get(x) == None else str(CardDict[x]))
print(" ".join(Output))