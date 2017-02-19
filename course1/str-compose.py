import sys

lines = sys.stdin.readlines()

l = int(lines[0])
line = lines[1]

def strCompose(line, length):
	return [line[i:i+length] for i in range(len(line)-length+1)]

for i in strCompose(line, l):
	print i