class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        strs_w_len = [str(len(s))+','+s for s in strs]
        res = ""
        for s in strs_w_len:
            res += '#' + s 
        return res
    def decode(self, s: str) -> List[str]:
        if not s: return []
        res = []
        curr_str = ""
        i = 0
        while i < len(s):
            num = ""
            if s[i] == '#':
                i = i+1
                while s[i] != ',':
                    num += s[i]
                    i += 1
                print(num)
                curr = s[i+1:i+int(num)+1]
                print(curr)
                res.append(curr)
                i += int(num)+1
            else:
                i += 1
        return res
                