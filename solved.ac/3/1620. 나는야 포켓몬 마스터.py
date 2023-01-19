import sys
input = sys.stdin.readline
PocketmonCount, QuestionCount = map(int, input().rstrip().split(' '))
PocketMons = [input().rstrip() for _ in range(PocketmonCount)]
PocketMonDict = {}
for i, name in enumerate(PocketMons):
	PocketMonDict[name] = i + 1
for _ in range(QuestionCount):
	InputData = str(input().rstrip())
	if not InputData.isdigit():
		print(PocketMonDict[InputData])
	else:
		# Num
		InputData = int(InputData) - 1
		print(PocketMons[InputData])