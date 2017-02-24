import sys

lines = sys.stdin.readlines()

l = int(lines[0])
line = lines[1]

def strCompose(line, length):
	"""
	Code Challenge: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).
	"""
	return [line[i:i+length] for i in range(len(line)-length+1)]

for i in strCompose(line, l):
	print i