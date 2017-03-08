import sys

lines = sys.stdin.readlines()
k, d = [int(i.strip()) for i in lines[0].split()]
kdmers = [line.strip() for line in lines[1:]]

def pairPathToText(pairs, k, d):
	firstHalf, secondHalf = pairs[0].split("|")
	for pair in pairs[1:]:
		firstHalf += pair[k-2]
		secondHalf += pair[-1]

	return firstHalf + secondHalf[-(k+d):]


print pairPathToText(kdmers, k, d)
