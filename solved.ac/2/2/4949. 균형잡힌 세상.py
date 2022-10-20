while True:
	a=input()
	if a==".":
		break
	s=[]
	e=False
	for x in a:
		if x=="[":
			s.append(False)
		elif x=="]":
			if len(s) == 0 or s[-1]!=False:
				print("no")
				e=True
				break
			else:
				s.pop()
		elif x=="(":
			s.append(True)
		elif x==")":
			if len(s) == 0 or s[-1]!=True:
				print("no")
				e=True
				break
			else:
				s.pop()
	if e==False:
		if len(s) == 0:
			print("yes")
		else:
			print("no")