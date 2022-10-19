def Recursion(c, l, r, cnt):
	cnt+=1
	if l >= r:
		return f"1 {cnt}"
	elif c[l] != c[r]:
		return f"0 {cnt}"
	else:
		return Recursion(c, l+1, r-1, cnt)

def IsPalindrome(c):
	return Recursion(c, 0, len(c) - 1, 00)

length=int(input())
for i in range(length):
	print(IsPalindrome(input()))