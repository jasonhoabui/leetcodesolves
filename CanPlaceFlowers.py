class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftopen = (i == 0 or flowerbed[i - 1] == 0)
                rightopen = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
                if leftopen and rightopen:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True
        
        return count >= n