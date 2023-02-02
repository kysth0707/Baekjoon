Words = []
ConvertDict = {}
ChangeWord = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,-:;!?"
ChangeWord += "'"
ChangeWord += '"'
print(ChangeWord)
for i, txt in enumerate(ChangeWord):
	ConvertDict[txt]=i
print(ConvertDict)

# def ConvertText(text : str):
# 	return [ConvertDict[x] for x in text]
	
WordList = []
with open(r'E:\GithubProjects\Baekjoon\solved.ac\21380\words_alpha.txt') as f:
	WordList = f.readlines()
# print(len(Words))
WordNumList = []
for i, word in enumerate(WordList):
	print(f"\r{i} / {len(WordList)} ...", end="")
	WordNumList.append([ConvertDict[x] for x in word[:-1]])
	if i == 100:
		break