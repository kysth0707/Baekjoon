import sys, heapq
def input():
	return sys.stdin.readline().rstrip()
n = int(input())
heap = list()
for _ in range(n):
	x = int(input())
	if x == 0:
		if not heap:
			print(0)
		else:
			print(heapq.heappop(heap)[1])
	else:
		heapq.heappush(heap, (-x, x))