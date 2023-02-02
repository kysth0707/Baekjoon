import sys
def input():
	return sys.stdin.readline().rstrip()
TestCaseCount = int(input())
for _ in range(TestCaseCount):
	Queue = []
	CalculateCount = int(input())
	PosDict = {}
	for _ in range(CalculateCount):
		Calculate, Num = input().split(' ')
		Num = int(Num)

		if Calculate == "I":
			Queue.append(Num)
			if PosDict.get(Num) == None:
				PosDict[Num] = [len(PosDict) - 1]
			else:
				PosDict[Num].append(len(PosDict) - 1)
		elif Calculate == "D":
			if len(Queue) > 0:
				if Num == 1:
					try:
						del Queue[PosDict[max(Queue)][0]]
					except:
						pass
				elif Num == -1:
					try:
						del Queue[PosDict[min(Queue)][0]]
					except:
						pass
	if len(Queue) == 0:
		print("EMPTY")
	else:
		print(max(Queue), min(Queue))

