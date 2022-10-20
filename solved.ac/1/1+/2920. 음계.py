import sys
input = sys.stdin.readline
a="".join(list(map(str, input().split(' '))))[:-1]
if a=="12345678":
	print("ascending")
elif a=="87654321":
	print("descending")
else:
	print("mixed")