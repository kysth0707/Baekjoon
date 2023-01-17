import sys
input = sys.stdin.readline
height, width, item = map(int, input().rstrip().split(' '))
Map = [list(map(int, input().rstrip().split(' '))) for _ in range(height)]
BestTime = int(1e9)
BestY = 0
minVal = min(map(min, Map))
maxVal = max(map(max, Map)) + 1
for yHeight in range(minVal, maxVal):
	Time = 0
	ItemCount = item
	for y in range(height):
		for x in range(width):
			val = (Map[y][x] - yHeight)
			Time += val * 2 if val > 0 else -val
			ItemCount += val
	if ItemCount > 0:
		continue
	if Time <= BestTime:
		# print(yHeight, ItemCount, Time)
		BestTime = Time
		BestY = yHeight
print(BestTime, BestY)