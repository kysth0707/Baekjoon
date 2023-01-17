a=[i+1 for i in range(int(input()))]
while True:
	print(a)
	a.pop(0)
	print(a)
	a.append(a[0])
	a.pop(0)
	if len(a) == 1:
		break
print(a[0])

# 1234
# 234
# 342
# 42
# 4

# 12345
# 2345
# 3452
# 452
# 524
# 24
# 42
# 4