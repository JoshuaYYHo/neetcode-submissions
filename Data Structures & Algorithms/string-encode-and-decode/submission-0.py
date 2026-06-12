class Solution:

    def encode(self, strs: List[str]) -> str:
        # Should be cesar cipher

        res = ""
        for i in range(len(strs)):
            
            # my encoder
            length = len(strs[i])

            res += str(length) + "#"+ strs[i]

        return res




    def decode(self, s: str) -> List[str]:
        
        # Just remove the first character which is always the length (delimeter)

        returned_list, i = [], 0

        while i < len(s):
            
            # Which is the length of the str
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            curr = s[j + 1 : j+ 1 + length]
            returned_list.append(curr)

            i = j + 1 + length

        return returned_list