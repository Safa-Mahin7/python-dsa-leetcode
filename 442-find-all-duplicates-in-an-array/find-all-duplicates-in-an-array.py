class Solution:
    def findDuplicates(self, nums):
        result = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] *= -1

        return result