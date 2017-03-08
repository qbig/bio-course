import sys

lines = sys.stdin.readlines()

dna = lines[0].strip()

amino = lines[1].strip()

codon = lines[2:]

RNAaminoDict = {}
aminoRNADict = {}
for l in codon:
	pair = l.strip().split()
	if len(pair) == 2:
		RNAaminoDict[pair[0]] = pair[1]
		if pair[1] not in aminoRNADict:
			aminoRNADict[pair[1]] = [pair[0]]
		else:
			aminoRNADict[pair[1]].append(pair[0])
	else:
		RNAaminoDict[pair[0]] = ""

dnaPairs = {
	"A" : "T",
	"T" : "A",
	"G" : "C",
	"C" : "G"
}

def RNAChar(c):
	if c == "T":
		return "U"
	else:
		return c

def DNAInverse(dna):
	return "".join([dnaPairs[c] for c in dna])

def toRNA(dna):
	return "".join([RNAChar(c) for c in dna])

def possibleRNA(amino):
	result = []
	possibleRNAHelper("", [aminoRNADict[c] for c in amino], len(amino)*3, result)
	return result

def possibleRNAHelper(accu, aminoRNAs, size, result):
	if len(accu) == size:
		result.append(accu)
		return

	for rna in aminoRNAs[0]:
		possibleRNAHelper(accu+rna, aminoRNAs[1:], size, result)

def matchRNAs(substr, possibleRNAs):
	for rna in possibleRNAs:
		if rna == substr:
			return True
	return False

def aminoToDNA(amino, dna):
	result = []
	RNA = toRNA(dna)
	reverseRNA = "".join(list(reversed(toRNA(DNAInverse(dna)))))
	possibleRes = possibleRNA(amino)
	expectedSize = 3 * len(amino)
	for i in range(len(dna)+1 - expectedSize):
		if matchRNAs(RNA[i:i+expectedSize], possibleRes):
			result.append(dna[i:i+expectedSize])
		elif matchRNAs(reverseRNA[i:i+expectedSize], possibleRes):
			result.append(dna[-(i+expectedSize):-i])
	return result

for res in  aminoToDNA(amino, dna):
	print res







