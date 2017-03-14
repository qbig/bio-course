import sys

lines = sys.stdin.readlines()

amount = int(lines[0])
coins = [int(i) for i in lines[1].strip().split(",")]


class Solution(object):
    def __init__(self, amount, coins):
        self.min = {}
        self.amount = amount
        self.coins = coins

    def helper(self, remain):
        if remain in self.min:
            return self.min[remain]

        if remain in self.coins:
            return 1

        nextVals = [self.helper(remain - coinVal) + 1 for coinVal in self.coins if remain - coinVal > 0]
        self.min[remain] = min(nextVals)
        return self.min[remain]

    def solve(self):
        return self.helper(self.amount)


class SolutionIterative(object):
    def __init__(self, amount, coins):
        self.min = {}
        self.amount = amount
        self.coins = coins

    def solve(self):
        dp = [999999] * (self.amount + 1)
        for coinVal in self.coins:
        	if coinVal < self.amount:
        		dp[coinVal] = 1

        for i in range(1, self.amount+1):
        	for coinVal in self.coins:
        		if i - coinVal > 0 and dp[i - coinVal] + 1 < dp[i]:
        			dp[i] = dp[i - coinVal] + 1
        
        return dp[-1]
        
print Solution(amount, coins).solve()
print SolutionIterative(amount, coins).solve()
