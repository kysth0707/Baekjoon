import sys
a=int(input())
b=[sys.stdin.readline().rstrip() for i in range(a)]
b=list(set(b))
b.sort(key=lambda x:(len(x), x))
print("\n".join(b))