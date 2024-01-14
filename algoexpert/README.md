# algoexpert problems

<details>
<summary>1. Two-sum problem</summary>

Given a list of numbers and a target sum, find if any two numbers in the array sum up to the target sum.

**Solution 1 - HashSet: (Time complexity: O(n), Space complexity: O(n))**

Initialize a hash set. Check if the diff(target sum - curr element) exists in the set. If yes, then we found the two numbers, else keep iterating until we add all numbers to the set.

**Solution 2 - Two pointer method: (Time complexity: O(n), Space complexity: O(n))**

Sort the array in nlog(n) time. Initialize two pointers on the beginning and end of the sorted array. If `curr sum < target sum`, then move the left pointer to right. If `curr sum > target sum`, we need to reduce the sum, move right pointer towards left. If `curr sum = target sum`, we are done. If left and right pointers cross, then no two numbers in the array will give the target sum.
</details>

<details>
<summary>2. Find closest value in a BST</summary>
Given a BST and a target integer value, find the closest value to the target value contained in the BST.

**Solution 1 - Recursive approach**


</details>



