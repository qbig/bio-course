import sys

lines = sys.stdin.readlines()

def spell(kmers):
	return kmers[0].strip() + "".join([kmer.strip()[-1] for kmer in kmers[1:]])


print spell(lines)