#find kids with greatest number of candles
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):#function to find kids with greatest number of candles
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)#find the maximum number of candies
        return [candy + extraCandies >= max_candies for candy in candies]#return the kids with the greatest number of candies by adding the extra candies to the candies and checking if they are greater than or equal to the maximum number of candies
    