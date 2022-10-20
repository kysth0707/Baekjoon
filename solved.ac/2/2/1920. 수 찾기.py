input()
b=set(map(int,input().split(' ')))
input()
d=list(map(int,input().split(' ')))
for x in d:
	print(1 if x in b else 0)