class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        std::sort(nums.begin(), nums.end());
        int n = nums.size();

        long long closest_sum = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < n - 2; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int min_possible = nums[i] + nums[i + 1] + nums[i + 2];

            if (min_possible > target) {
                if (std::abs(min_possible - target) < std::abs(closest_sum - target)) {
                    closest_sum = min_possible;
                }
                break; // Subsequent sums will only get larger and further away
            }

            int max_possible = nums[i] + nums[n - 2] + nums[n - 1];
            if (max_possible < target) {
                if (std::abs(max_possible - target) < std::abs(closest_sum - target)) {
                    closest_sum = max_possible;
                }
                continue; // Skip to next 'i'
            }

            int left = i + 1;
            int right = n - 1;
        
            while (left < right) {
                int current_sum = nums[i] + nums[left] + nums[right];
            
                // Optimization 4: Exact match found
                if (current_sum == target) {
                    return current_sum;
                }
                
                if (std::abs(current_sum - target) < std::abs(closest_sum - target)) {
                    closest_sum = current_sum;
                }
                
                if (current_sum < target) {
                    left++;
                // Optimization 5: Skip duplicate left elements
                    while (left < right && nums[left] == nums[left - 1]) left++;
                } else {
                    right--;
                // Optimization 6: Skip duplicate right elements
                    while (left < right && nums[right] == nums[right + 1]) right--;
                }
            }
        }
    
        return closest_sum;

    }
};