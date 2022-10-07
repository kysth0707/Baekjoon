Length = int(input())
List = list(map(int, input().split(' ')))
Result = 0
Max = max(List)
for i in range(Length):
	Result += List[i] / Max * 100
print(Result / Length)