import sys
def input():
	return sys.stdin.readline().rstrip()
TestCaseCount = int(input())
for _ in range(TestCaseCount):
	Queue = []
	CalculateCount = int(input())
	for _ in range(CalculateCount):
		Calculate, Num = input().split(' ')
		Num = int(Num)

		if Calculate == "I":
			Queue.append(Num)
		elif Calculate == "D":
			if len(Queue) > 0:
				if Num == 1:
					Queue.remove(max(Queue))
				elif Num == -1:
					Queue.remove(min(Queue))
	if len(Queue) == 0:
		print("EMPTY")
	else:
		print(max(Queue), min(Queue))

