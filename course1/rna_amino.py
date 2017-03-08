import sys

lines = sys.stdin.readlines()

rna = lines[0].strip()

codon = lines[1:]

dic = {}
for l in codon:
	pair = l.strip().split()
	if len(pair) == 2:
		dic[pair[0]] = pair[1]
	else:
		dic[pair[0]] = ""

def rnaToAmino(rna):
	return "".join([dic[rna[i:i+3]] for i in range(0, len(rna), 3)])

print rnaToAmino(rna)