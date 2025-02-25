class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in accounts:
            total = sum(i)
            richest = max(richest, total)
        return richest