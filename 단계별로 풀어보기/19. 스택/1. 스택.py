import sys
Length = int(input())

stack = []
for i in range(Length):
	cmd = sys.stdin.readline().split()
	if cmd[0] == "push":
		stack.append(int(cmd[1]))
	elif cmd[0] == "pop":
		print(stack.pop() if len(stack) > 0 else -1)
	elif cmd[0] == "size":
		print(len(stack))
	elif cmd[0] == "empty":
		print(0 if len(stack) > 0 else 1)
	elif cmd[0] == "top":
		print(stack[-1] if len(stack) > 0 else -1)