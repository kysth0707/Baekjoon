num=int(input())
numsave=num
cycle=0
while True:
	cycle+=1
	a=num//10
	b=num%10
	c=(a+b)%10
	num = (b*10)+c
	if num == numsave:
		break
print(cycle)