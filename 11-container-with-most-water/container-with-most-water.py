class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxWater = 0
        while(left<right):
            width = right - left
            minHeight = min(height[left], height[right])

            area = width * minHeight

            maxWater = max(maxWater, area)

            if (left == right): 
                return left, right
            elif (height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxWater
        
        