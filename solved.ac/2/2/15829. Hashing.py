input()
a=input()
b=0
c=0
d="abcdefghijklmnopqrstuvwxyz"

for x in a:
	c += (d.find(x) + 1) * 31 ** b
	b += 1
print(c%1234567891)