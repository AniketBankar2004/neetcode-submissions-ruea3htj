class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        n = len(s)
        seen = set()
        for r  in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l = l+1
            seen.add(s[r])
            cur_len = (r - l) +1
            max_len = max(cur_len,max_len)
        return max_len

