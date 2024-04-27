class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,4,5,6,1]
    res1 = sol.containsDuplicate(nums1)
    nums2 = [1,2,3,4]
    res2 = sol.containsDuplicate(nums2)

    print(f"{nums1} = {res1}")
    print(f"{nums2} = {res2}")