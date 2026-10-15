class Solution(object):
    def fourSum(self, nums, target):
        
        nums.sort()  # Step 1: Sort the array to use pointers effectively
        n = len(nums)
        results = []

    # Pointer 1: Outer loop
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue  # Skip duplicates for Pointer 1
            
        # Pointer 2: Second loop
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    continue  # Skip duplicates for Pointer 2

            # Pointer 3 (left) and Pointer 4 (right) moving inward
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates
                        while left < right and nums[left] == nums[left + 1]: 
                            left += 1
                        while left < right and nums[right] == nums[right - 1]: 
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1  # Sum is too small, move left pointer right
                    else:
                        right -= 1 # Sum is too big, move right pointer left

        return results

            