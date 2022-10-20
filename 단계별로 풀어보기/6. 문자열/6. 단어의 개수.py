Result = input().split(' ')
if Result[0] == '':
	del Result[0]
if Result[len(Result) - 1] == '':
	del Result[len(Result) - 1]
print(len(Result))
