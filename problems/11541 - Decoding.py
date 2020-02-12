testcase = int(input())
for i in range(testcase+1):
	if i == 0:
		continue
	strlist = input()
	strlen = len(strlist)
	j = 0
	decodestr = "Case {}: ".format(i)
	while j < strlen:
		ch = strlist[j]
		if ch == '\n':
			break
		else:
			cnt = 0
			k = j + 1
			while(k < strlen and strlist[k].isdigit()):
				cnt *= 10
				cnt += int(strlist[k])
				k += 1
			decodestr += ch * cnt
			j = k
	print(decodestr)