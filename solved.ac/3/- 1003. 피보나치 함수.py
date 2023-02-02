import sys
def input():
	return sys.stdin.readline().rstrip()
TestCaseCount = int(input())
def fibonacci(n : int):
	if n != 0 and n != 1:
		return fibonacci(n-1) + fibonacci(n-2)
	else:
		return n
# def fibonacci(n : int):
# 	if n == 0:
# 		return (zeroCount + 1, oneCount)
# 	elif n == 1:
# 		return (zeroCount, oneCount + 1)
# 	else:
# 		a = fibonacci(n - 1, zeroCount, oneCount)
# 		b = fibonacci(n - 2, zeroCount, oneCount)
# 		return (a[0]+b[0], a[1]+b[1])

print(fibonacci(int(input())))
for i in range(TestCaseCount):
	a=int(input())
	print(fibonacci(a-1), fibonacci(a))