import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

text = lines[0]

res_val = 0
min_val = 9999999
res = [res_val]
for i in text:
	if i == "G":
		res_val += 1
	if i == "C":
		res_val -= 1
	res.append(res_val)
	if res_val < min_val:
		min_val = res_val
	print res_val ,

print 
for i, val in enumerate(res):
	if val == min_val:
		print i


		
