import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

line = lines[0]
k = int(lines[1])

def countPattern(line, pattern):
	pat_len = len(pattern)
	cnt = 0
	for i in range(len(line)-pat_len+1):
		if line[i:i+pat_len] == pattern:
			cnt += 1

	return cnt

def frequentWord(line, k):
	result = []
	max_cnt = 0
	for i in range(len(line)-k+1):
		l = countPattern(line, line[i:i+k])
		if l > max_cnt:
			max_cnt = l
	for i in range(len(line)-k+1):
		l = countPattern(line, line[i:i+k])
		if l == max_cnt:
			result.append(line[i:i+k])
	return list(set(result))

print frequentWord(line, k)

