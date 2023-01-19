import sys
input = sys.stdin.readline
TestCaseCount = int(input().rstrip())
for _ in range(TestCaseCount):
	Func = str(input().rstrip())
	ArrayLength = int(input().rstrip())
	try:
		Array = list(map(int, input().rstrip()[1:-1].split(',')))
	except:
		Array = []

	IsFront = True
	IsError = False
	for fun in Func:
		if fun == "R":
			IsFront = not IsFront
		elif fun == "D":
			if len(Array) == 0:
				IsError = True
				break
			else:
				del Array[0 if IsFront else len(Array) - 1]
	if not IsFront:
		Array = Array[::-1]
	if IsError:
		print("error")
	else:
		print("[" + ",".join(map(str, Array)) + "]")
