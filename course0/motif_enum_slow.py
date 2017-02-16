import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k, d = [int(i) for i in lines[0].split()]

DNAs = lines[1:]

def hamming(x, y):
	res = 0
	for i, c in enumerate(x):
		if c != y[i]:
			res += 1
	return res

def proxiEqual(x, y, d):
	return hamming(x, y) <= d

def getNeighbour(text, d):
	if d == 0:
		return [text]

	if len(text) == 1:
		return ["A", "T", "G", "C"]

	neighours = []
	suffix = text[1:]
	suffix_neighours = getNeighbour(suffix, d)
	for t in suffix_neighours:
		if hamming(t, suffix) < d:
			neighours += [x + t for x in ["A", "T", "G", "C"]]
		else:
			neighours.append(text[0] + t) 

	return neighours


def containsWithD(text, pattern, k, d):
	for i in range(len(text)-k+1):
		if pattern in getNeighbour(text[i:i+k], d):
			return True

	return False

def motifEnumerate(DNAs, k, d):
	res = []
	for cur_dna in DNAs:
		others = DNAs[:]
		others.remove(cur_dna)
		for i in range(len(cur_dna) - k + 1):
			pattern = cur_dna[i:i+k]
			for pattern_with_d in getNeighbour(pattern, d):
				if all([containsWithD(dna, pattern_with_d, k, d) for dna in others]):
					res.append(pattern_with_d)
	return list(set(res))

for motif in motifEnumerate(DNAs, k, d):
	print motif ,
