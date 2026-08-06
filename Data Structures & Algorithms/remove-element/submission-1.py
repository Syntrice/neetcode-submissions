class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        pointerA = 0;

        for pointerB in range(n):
            if (nums[pointerB] != val):
                swap = nums[pointerA]
                nums[pointerA] = nums[pointerB]
                nums[pointerB] = swap
                pointerA += 1

        return pointerA

                
