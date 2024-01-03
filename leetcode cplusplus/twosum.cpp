#include <vector>
#include <unordered_map>
#include <iostream>
using std::unordered_map;
using std::vector;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {

        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (map.count(complement) == 1)
            {
                return {i, map[complement]};
            }
            else
            {
                map[nums[i]] = i;
            }
        }
        return {-1, -1};
    };
};

int main(){
    Solution sol;

    vector<int> nums = {1,2,3,4,5,6,7};
    int target=13;

    vector<int> result = sol.twoSum(nums,target);

    for (int i:result){
        std::cout << i << " ";
    }

}