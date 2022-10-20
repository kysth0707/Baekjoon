List = []
for i in range(10):
	List.append(int(input()) % 42)
print(len(list(set(List))))
