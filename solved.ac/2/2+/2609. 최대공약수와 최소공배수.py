# https://velog.io/@jwisgenius/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
a,b=map(int,input().split(' '))
if a<b:
	a,b=b,a
def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a
def lcm(a, b):
	return int(a * b / gcd(a, b))
print(gcd(a,b))
print(lcm(a,b))