import sys
input = sys.stdin.readline
SiteCount, SiteSearchCount = list(map(int, input().rstrip().split(' ')))
SiteDict = {}
for _ in range(SiteCount):
	SiteName, Password = input().rstrip().split(' ')
	SiteDict[SiteName] = Password
for _ in range(SiteSearchCount):
	print(SiteDict[input().rstrip()])