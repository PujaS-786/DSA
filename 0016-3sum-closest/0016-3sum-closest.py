class Solution(object):
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        n = len(nums)

        # Initialize with the first valid triplet sum instead of infinity
        closest_sum = nums[0] + nums[1] + nums[2]
    
        for i in range(n - 2):
            # Optimization 1: Skip duplicate values for the first pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization 2: Smallest possible sum with the current nums[i]
            # If even this largest impossible gap is too big, we can check it and move on
            min_possible = nums[i] + nums[i + 1] + nums[i + 2]
            if min_possible > target:
                if abs(min_possible - target) < abs(closest_sum - target):
                    closest_sum = min_possible
                # Since nums is sorted, all subsequent sums in this loop will be even larger/further away
                break 
            
            # Optimization 3: Largest possible sum with the current nums[i]
            max_possible = nums[i] + nums[n - 2] + nums[n - 1]
            if max_possible < target:
                if abs(max_possible - target) < abs(closest_sum - target):
                    closest_sum = max_possible
                continue # Skip to the next 'i' because no combinations here can reach the target
            
            # Two-pointer approach
            left = i + 1
            right = n - 1
        
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                # Optimization 4: Exact match found, terminate instantly
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                    # Optimization 5: Skip duplicate left elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # Optimization 6: Skip duplicate right elements
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return closest_sum