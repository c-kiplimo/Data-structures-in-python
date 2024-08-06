#class

class Solution:
    def max_area(self,heights):
        left,right=0,len(heights)-1
        max_area=0

        while left < right:
            height=min(heights[left],heights[right])
            width = right-left

            current_area=height * width

            max_area=max(max_area,current_area)

            if heights[left] < heights[right] :
                left +=1
        
            else:
                right -=1
        
        return max_area
    
solution =Solution()

print(solution.max_area([3,5,6,7,3,2,9]))



