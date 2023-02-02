import sys
def input():
	return sys.stdin.readline().rstrip()
n,m=map(int, input().split(' '))
Dict = {}
for _ in range(n):
	Dict[input()]=False
cnt = 0
for _ in range(m):
	x = input()
	if Dict.get(x) == False:
		Dict[x] = True
		cnt += 1
print(cnt)
for key, value in Dict.items():
	if value == True:
		print(key)