class Solution:
    def three_sum(self, nums):
        nums.sort()
        result = []

        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 1):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                target = -(nums[i] + nums[j])

                left = j + 1
                right = n - 1

                while left <= right:
                    mid = (left + right) // 2

                    if nums[mid] == target:
                        result.append(
                            [nums[i], nums[j], nums[mid]]
                        )
                        break

                    elif nums[mid] < target:
                        left = mid + 1

                    else:
                        right = mid - 1

        return result