# 버그
# https://www.acmicpc.net/problem/2941

Dicts = {'c=' : 'č' ,'c-' : 'ć','dz=' : 'dž','d-' : 'đ','lj' : 'lj','nj' : 'nj','s=' : 'š','z=' : 'ž'}
Data = input()
Count = 0
for key in Dicts.keys():
	while True:
		if key in Data:
			Data = Data.replace(key, Dicts[key], 1)
			Count += 1
		else:
			break
		print(key, Data)
print(Count, Data)