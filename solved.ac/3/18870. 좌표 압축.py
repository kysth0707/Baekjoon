import sys
input = sys.stdin.readline
PosCount = int(input().rstrip())
OriginalPosList = list(map(int,input().rstrip().split(' ')))

SortedPosList = sorted(list(set(OriginalPosList)))
PostDict = {data : i for i, data in enumerate(SortedPosList)}
print(" ".join(map(str, list(PostDict[pos] for pos in OriginalPosList))))