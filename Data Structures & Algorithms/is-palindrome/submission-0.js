class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0, r = s.length-1
        while(r > l){
            while (l < r && !this.alphaNum(s[l])) {
                l++;
            }
            while (r > l && !this.alphaNum(s[r])) {
                r--;
            }
            if (s[r].toLowerCase() !== s[l].toLowerCase()){
                return false
            }
            l++;
            r--; 
        }
        return true
    }

    alphaNum(c) {
        const charCode = c.charCodeAt(0);
        return (
            (65 <= charCode && charCode <= 90) ||
            (97 <= charCode && charCode <= 122) ||
            (48 <= charCode && charCode <= 57)
        );
    }
}
