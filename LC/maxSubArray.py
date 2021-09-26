from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0
        res = 0

        for num in nums:
            sum += num

            res = max(sum, res)

            if sum < 0:
                sum = 0

        return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()

print(solution.maxSubArray(nums))
