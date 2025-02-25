class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x < 10:
            return x
        x = str(x)
        first = x[0]
        second = x[1]
        x = int(x)
        if x % (int(first) + int(second)) == 0:
            return int(first) + int(second)
        return -1