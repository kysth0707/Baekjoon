n, r, c = map(int, input().split(' '))

#    +1 +3
# 0 1 4 5 16 17 20 21
# 0 1 2 3 4  5  6  7

# +2
# +6
x = 0
for i in range(r + 1):
	if i%2 == 0:
		x += 1
	else:
		x += 3

for i in range(c):
	if i%2 == 0:
		x += 2
	else:
		x += 6
print(x)