class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        std::vector<std::vector<int>> result;
        int n = nums.size();

        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; ++i) { 
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            if (nums[i] > 0) {
                break;
            }

            int left = i + 1;
            int right = n - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    // Correct nested brace syntax: adds a vector<int> to vector<vector<int>>
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicates for the second position
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    // Skip duplicates for the third position
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    // Move both pointers inward after finding a valid triplet
                    left++;
                    right--;
                } 
                else if (sum < 0) {
                    left++; // Sum is too small, move left pointer to increase sum
                } 
                else {
                    right--; // Sum is too large, move right pointer to decrease sum
                }
            }
        }
        
        return result;
    }
};