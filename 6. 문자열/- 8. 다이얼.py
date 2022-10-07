# 나중에 시도하기
# https://www.acmicpc.net/problem/5622
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetNum = [3,3,3,3,3,4,3,4]

Data = input()
Output = 0
for i in range(len(Data)):
	for ii in range(len(alphabets)):
		if Data[i].find(alphabets[ii]) != -1:
			Sum = 0
			for x in range(len(alphabetNum)):
				if alphabetNum[x] + Sum > ii:
					Output += 2 + x
					break
				Sum += alphabetNum[x]
print(Output)