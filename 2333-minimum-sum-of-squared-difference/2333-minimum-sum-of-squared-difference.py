class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        
        n = len(nums1)
        k = k1 + k2
    
    # Step 1: Calculate absolute differences
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_diff = max(diffs)
    
    # If the maximum difference is already 0, the sum of squared differences is 0
        if max_diff == 0:
            return 0
        
    # Step 2: Create a frequency array (bucket) for differences
    # bucket[d] stores how many pairs have an absolute difference equal to 'd'
        bucket = [0] * (max_diff + 1)
        for d in diffs:
            bucket[d] += 1
        
    # Step 3: Greedily reduce the largest differences from top to bottom
        for d in range(max_diff, 0, -1):
            if bucket[d] == 0:
                continue
            
        # Count of current maximum differences we want to reduce
            count = bucket[d]
        
        # If we have enough total 'k' operations to reduce ALL elements of size 'd' down to 'd-1'
            if k >= count:
                k -= count
                bucket[d - 1] += count
                bucket[d] = 0
            else:
            # We can only reduce 'k' of them down to 'd-1'
                bucket[d - 1] += k
                bucket[d] -= k
                k = 0
                break  # No operations left, exit early

    # Step 4: Calculate the final sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if bucket[d] > 0:
                ans += bucket[d] * (d ** 2)
            
        return ans

        