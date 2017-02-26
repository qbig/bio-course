import sys

lines = [l.strip() for l in sys.stdin.readlines()]

"""
Code Challenge: Solve the String Spelled by a Genome Path Problem.

Sample Input:
ACCGA
CCGAA
CGAAG
GAAGC
AAGCT

Sample Output:
ACCGAAGCT
"""

def spell(kmers):
	return kmers[0].strip() + "".join([kmer.strip()[-1] for kmer in kmers[1:]])


print spell(lines)