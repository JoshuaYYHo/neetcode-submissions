class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0

        sett = set()

        n = len(s)

        # O(n)
        for r in range(n):
            # We are trying to add in set so it's invalid
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            # so now valid window
            w = (r - l) + 1
            longest = max(longest, w)

            sett.add(s[r])

        return longest


        