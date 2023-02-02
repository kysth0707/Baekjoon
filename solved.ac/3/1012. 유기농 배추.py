import sys
def input():
	return sys.stdin.readline().rstrip()

def GetStartPos():
	for y in range(Height):
		for x in range(Width):
			if Map[y][x] != 0:
				return (x,y)
	return (-1, -1)

def CanGo(x,y):
	if x < 0 or y < 0 or x >= Width or y >= Height:
		return False
	if Map[y][x] == 1:
		return True
	else:
		return False

def FillMap(StartX,StartY):
	Spread = [(StartX,StartY)]
	while True:
		New = []
		for x, y in Spread:
			if Map[y][x] == 0:
				continue
			Map[y][x] = 0
			if CanGo(x + 1, y):
				New.append((x + 1, y))
			if CanGo(x - 1, y):
				New.append((x - 1, y))
			if CanGo(x, y + 1):
				New.append((x, y + 1))
			if CanGo(x, y - 1):
				New.append((x, y - 1))
		if len(New) == 0:
			break
		Spread = New


Map = None
	
TestCaseCount = int(input())
for _ in range(TestCaseCount):
	Width, Height, BaechuCount = map(int, input().split(' '))
	Map = [[0] * Width for _ in range(Height)]

	for __ in range(BaechuCount):
		x,y = map(int,input().split(' '))
		Map[y][x] = 1

	FillCount = 0
	while True:
		StartPos = GetStartPos()
		if StartPos == (-1, -1):
			break
		FillMap(StartPos[0], StartPos[1])
		FillCount += 1
	print(FillCount)