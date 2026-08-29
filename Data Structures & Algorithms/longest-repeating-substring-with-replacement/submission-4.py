class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = res = l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # 若当前窗口不能再替换符合法规矩 ingrediënten Hod
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # 移出左指针的影响
                l += 1  # 左指针右移

            res = max(res, r - l + 1)
        
        return res