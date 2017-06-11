def longestCommonPrefix(strs):
	if strs == []:
		return ""
	charList = []
	shortest = float('inf')
	for x in strs:
		charList.append(list(x))
		if len(x) < shortest:
			shortest = len(x)
	charListT = [[] for i in range(shortest)]
	for i, x in enumerate(charList):
		for j in range(shortest):
			charListT[j].append(x[j])
	setList = [len(set(x)) for x in charListT]
	flag = 0
	for x in setList:
		if x == 1:
			flag += 1
		else:
			break
	return strs[0][:flag]



tt1 = []
tt2 = ["aaa", "bbb"]
tt3 = ["aaa", "aab", "aac"]
tt4 = ["aaa", "aab", "acc"]
tt5 = ["shdfkgsakhfg"]
tt6 = [""]


print longestCommonPrefix(tt1)
print longestCommonPrefix(tt2)
print longestCommonPrefix(tt3)
print longestCommonPrefix(tt4)
print longestCommonPrefix(tt5)
print longestCommonPrefix(tt6)