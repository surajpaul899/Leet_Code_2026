
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            new = target - nums[i]

            if new in seen:
                return [seen[new], i]

            seen[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))
