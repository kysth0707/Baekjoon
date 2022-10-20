import sys
Length = int(sys.stdin.readline())

stack = []
for i in range(Length):
	a = int(sys.stdin.readline())
	if a == 0:
		stack.pop()
	else:
		stack.append(a)
print(sum(stack))