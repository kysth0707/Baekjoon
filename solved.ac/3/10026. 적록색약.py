import sys, copy
input = sys.stdin.readline
Height = int(input().rstrip())
Map = [list(input().rstrip()) for _ in range(Height)]
Width = len(Map[0])
# 이미 정해진 구역은 0 으로 설정하겠습니다
def GetStartPos():
	for y in range(Height):
		for x in range(Width):
			if Map[y][x] != "0":
				return (x,y)
	return (-1, -1)

def CanGo(x,y, RGBValue):
	if x < 0 or y < 0 or x >= Width or y >= Height:
		return False
	if Map[y][x] == RGBValue:
		return True
	else:
		return False

# def ShowMap():
# 	print("-=========-")
# 	for y in range(Height):
# 		for x in range(Width):
# 			print(Map[y][x],end='')
# 		print("")

def FillMap(StartX,StartY):
	Spread = [(StartX,StartY)]
	while True:
		New = []
		for x, y in Spread:
			if Map[y][x] == "0":
				continue
			CurrentRGB = Map[y][x]
			Map[y][x] = "0"
			if CanGo(x + 1, y, CurrentRGB):
				New.append((x + 1, y))
			if CanGo(x - 1, y, CurrentRGB):
				New.append((x - 1, y))
			if CanGo(x, y + 1, CurrentRGB):
				New.append((x, y + 1))
			if CanGo(x, y - 1, CurrentRGB):
				New.append((x, y - 1))
		if len(New) == 0:
			break
		Spread = New
		
FillCount = 0
MapSave = copy.deepcopy(Map)
while True:
	StartPos = GetStartPos()
	if StartPos == (-1, -1):
		break
	FillMap(StartPos[0], StartPos[1])
	FillCount += 1
	# ShowMap()
print(FillCount,end=' ')

Map = MapSave
for y in range(Height):
	for x in range(Width):
		if Map[y][x] == "R":
			Map[y][x] = "G"
FillCount = 0
while True:
	StartPos = GetStartPos()
	if StartPos == (-1, -1):
		break
	FillMap(StartPos[0], StartPos[1])
	FillCount += 1
print(FillCount)