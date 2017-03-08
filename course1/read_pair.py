import sys

lines = sys.stdin.readlines()
k, d = [int(i.strip()) for i in lines[0].split()]
kdmers = [line.strip() for line in lines[1:]]

def prefix(kdmer):
	return "|".join([kmer[:-1] for kmer in kdmer.split("|")])

def suffix(kdmer):
	return "|".join([kmer[1:] for kmer in kdmer.split("|")])

print k, d
for kdmer in kdmers :
	print prefix(kdmer), "->", suffix(kdmer)




