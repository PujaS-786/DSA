class Solution(object):
    def threeSum(self, nums):

        result = []  # Correct list initialization
        nums.sort()  # Sort the list to use the two-pointer approach
        
        for i in range(len(nums)):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Append the triplet as a list
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    left += 1 # Sum is too small, move left pointer to increase sum
                else:
                    right -= 1 # Sum is too large, move right pointer to decrease sum
                    
        return result