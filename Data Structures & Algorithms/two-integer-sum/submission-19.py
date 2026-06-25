class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for count, element in enumerate(nums):
            remainder = target - element
            if remainder in hash_table:
                return [hash_table[remainder], count]
            else:
                hash_table[element] = count

