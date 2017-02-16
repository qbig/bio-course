import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

x = lines[0]
y = lines[1]

def hamming(x, y):
	res = 0
	for i, c in enumerate(x):
		if c != y[i]:
			res += 1
	return res

print hamming(x, y)
