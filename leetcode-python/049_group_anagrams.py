# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = {}

        for word in strs:
            key = "".join(sorted(word)) 

            if key in anagram_dict:
                anagram_dict[key].append(word)
            else:
                anagram_dict[key] = [word]

        return list(anagram_dict.values())
    
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    res = sol.groupAnagrams(strs)
    print(f"strs = {strs}, result = {res}")
