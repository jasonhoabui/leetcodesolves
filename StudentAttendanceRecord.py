class Solution:
    def checkRecord(self, s: str) -> bool:
        countabsent = 0
        countlate = 0
        for i in range(len(s)):
            if s[i] == "A":
                countabsent += 1
                countlate = 0
                if countabsent >= 2:
                    return False
            elif s[i] == "L":
                countlate += 1
                if countlate >= 3:
                    return False
            else:
                countlate = 0
        return True