import sys
input = sys.stdin.readline
CoinCount, Money = list(map(int, input().rstrip().split(' ')))
CoinList = [int(input().rstrip()) for _ in range(CoinCount)]
CoinUsedCount = 0
for i in range(CoinCount):
	CoinUsedCount += Money // CoinList[CoinCount - i - 1]
	Money = Money - (Money // CoinList[CoinCount - i - 1]) * CoinList[CoinCount - i - 1]
print(CoinUsedCount)