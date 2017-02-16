import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

line = lines[0]
def complement(line):
	result = ""
	for c in reversed(line):
		if c == "A":
			result += "T"
		elif c == "T":
			result += "A"
		elif c == "G":
			result += "C"
		elif c == "C":
			result += "G"

	return result

print complement(line)
