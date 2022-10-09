import sys
Length = int(sys.stdin.readline())

for _ in range(Length):
	a = sys.stdin.readline()
	
	stack = []
	Yes = True
	for txt in a:
		if txt == "(":
			stack.append(0)
		elif txt == ")":
			if len(stack) == 0:
				Yes = False
				break
			stack.pop()
	if len(stack) != 0:
		Yes = False
	print("YES" if Yes else "NO")