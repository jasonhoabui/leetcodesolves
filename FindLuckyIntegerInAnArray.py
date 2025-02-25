class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        lucky = []
        for i in arr:
            count[i] = count.get(i, 0) + 1
        for i in count:
            if count[i] == i:
                lucky.append(i) 
        if len(lucky) != 0:
            return max(lucky)
        return -1