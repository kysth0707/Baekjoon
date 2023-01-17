import copy
TestCaseCount = int(input())
def CanPrint(listvalue) -> bool:
	TargetValue = listvalue[0]
	for i in range(len(listvalue)):
		if listvalue[i] > TargetValue:
			return False
	return True

for _ in range(TestCaseCount):
	DocsCount, AskNum = map(int, input().split(' '))
	Docs = list(map(int, input().split(' ')))
	Counting = 0

	while True:
		if CanPrint(Docs):
			del Docs[0]
			if AskNum == 0:
				print("탈출!")
				break
		else:
			Docs.append(Docs[0])
			del Docs[0]
		print(Counting, Docs, AskNum)
		Counting += 1
		AskNum -= 1
		if AskNum < 0:
			AskNum = len(Docs) - 1
	print("ㅁㄴㅇㄹ", Counting)