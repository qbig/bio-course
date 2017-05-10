import sys


"""
    OutputLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return
        if backtracki, j = "↓"
            OutputLCS(backtrack, v, i - 1, j)
        else if backtracki, j = "→"
            OutputLCS(backtrack, v, i, j - 1)
        else
            OutputLCS(backtrack, v, i - 1, j - 1)
            output vi
"""

"""
Sample Input:
AACCTTGG
ACACTGTGA
Sample Output:
AACTGG
"""

lines = sys.stdin.readlines()
left, right = [l.strip() for l in lines]

def lcs_with_path(left, right):
	result = ""
	prev = {}
	l_left = len(left)
	l_right = len(right)

	score = [[0]*(l_right+1) for i in range(l_left+1)]
	for i in range(1, l_left+1):
		for j in range(1, l_right+1):
			up_val = score[i-1][j]
			left_val = score[i][j-1]
			diag_val = score[i-1][j-1]
			if left[i-1] == right[j-1]:
				diag_val += 1
			score[i][j] = max(up_val, left_val, diag_val)
			if score[i][j] == up_val:
				prev[(i,j)] = (i-1, j)
			elif score[i][j] == left_val:
				prev[(i,j)] = (i, j-1)
			else:
				prev[(i,j)] = (i-1, j-1)

	cursor = (l_left, l_right)
	while cursor != (0,0) and cursor[0] != 0 and cursor[1] != 0:
		prev_val = prev[cursor]
		if prev_val[0] == cursor[0] - 1 and prev_val[1] == cursor[1]-1:
			result = left[cursor[0] - 1] + result
		cursor = prev_val
		print(cursor)
	#print(prev)	
	return result
	#return score[l_left][l_right]


print(lcs_with_path(left,right))