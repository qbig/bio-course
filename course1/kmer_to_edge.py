import sys

lines = [l.strip() for l in sys.stdin.readlines()]

for kmer in lines :
	print kmer[:-1], "->", kmer[1:]




