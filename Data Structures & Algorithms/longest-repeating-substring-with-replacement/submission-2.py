class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, maxf, res = {}, 0, 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # 当前窗口的大小为 (r - l + 1)
            # 如果 (窗口大小 - 窗口中最多的字符数) > k，说明需要缩小窗口
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)  
        
        return res