class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_list = []

        for i in range(len(nums)):
            i_val = nums[i]
            for j in range(1, len(nums)):
                j_val = nums[j]

                if i == j:
                    break
                if i_val + j_val == target:
                    result_list.append(i)
                    result_list.append(j)
                    return result_list
