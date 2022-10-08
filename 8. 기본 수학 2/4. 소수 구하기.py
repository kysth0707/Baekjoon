def Dlist(Num):
	# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
	Primes = [True] * Num
	Primes[0] = False
	for i in range(2, int(Num ** 0.5) + 1):
		if Primes[i]:
			for x in range(2*i, Num, i):
				Primes[x] = False
	return [i for i in range(2, Num) if Primes[i] == True]
a,b=map(int, input().split(' '))
MyD = Dlist(b + 1)
for x in MyD:
	if x >= a:
		print(x)