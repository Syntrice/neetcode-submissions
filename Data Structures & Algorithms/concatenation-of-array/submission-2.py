class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (n * 2)
        for i, num in enumerate(nums):
            result[i]= num;
            result[i + n] = num;
        return result