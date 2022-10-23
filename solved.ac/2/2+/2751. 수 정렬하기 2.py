import sys
a=int(input())
b=[int(sys.stdin.readline().rstrip()) for i in range(a)]
b.sort()
print("\n".join(map(str,b)))