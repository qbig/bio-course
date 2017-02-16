import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

text = lines[0]
k, l, t = [int(i) for i in lines[1].split()]

gene = "ACGT"

def enum(res, accu, size):
    if len(accu) == size:
        res.append(accu)
        return
    
    for c in gene:
        enum(res, accu+c, size)

def computeFrequencyArr(text, k):
	patterns_arr = []
	enum(patterns_arr,"", k)
	res = [0] * len(patterns_arr)

	for i in range(len(text) - k + 1):
		res[patterns_arr.index(text[i:i+k])] += 1
	return res


# for i in  computeFrequencyArr(text, k):
# 	print i ,




arr = "GAGTTGTCCGCGTTCAT"

res = 0
for i, c in enumerate(reversed(arr)):
	res += gene.index(c) * (4**i)

def patternToNum(pat):
	if len(pat) == 1:
		return "ACGT".index(pat)
	
	return "ACGT".index(pat[-1]) + patternToNum(pat[:-1]) * 4


def numToPattern(index, k):
	if k == 1:
		return "ACGT"[index]

	prefix_index = index / 4
	remainder = index % 4
	symbol = "ACGT"[remainder]
	
	return numToPattern(prefix_index, k-1) + symbol

def findClumps(text, k, l, t):
	dic = {}
	for i in range(l-k+1):
		if text[i:i+k] in dic:
			dic[text[i:i+k]] +=1
		else :
			dic[text[i:i+k]] = 1
	res = []
	for key in dic:
		if dic[key] >= t:
			res.append(key)

	for i in range(1, len(text)-l+1):
		dic[text[i-1:i-1+k]] -=1
		if text[l+i-k:l+i] in dic:
			dic[text[l+i-k:l+i]] += 1
		else:
			dic[text[l+i-k:l+i]] = 1

		for key in dic:
			if dic[key] >= t:
				res.append(key)

	return list(set(res))

print findClumps(text, k,l,t)