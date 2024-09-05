class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

obj = Solution()

print(obj.isAnagram(s="Hello", t="olleh"))  