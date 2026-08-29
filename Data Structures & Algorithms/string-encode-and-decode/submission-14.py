import json

class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(json.dumps(s) + '\0' for s in strs)
    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        offset = 0
        while True:
            try:
                end = s.index('\0', offset)
                item = json.loads(s[offset:end])
                res.append(item)
                offset = end + 1
            except ValueError:
                if offset == 0:
                    return []  # 说明输入为空字符串
                break
        return res