import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

line = lines[0]
pattern = lines[1]

len_pat = len(pattern)
for i in range(len(line) - len(pattern)+1):
	if pattern == line[i:i+len_pat]:
		print i ,
