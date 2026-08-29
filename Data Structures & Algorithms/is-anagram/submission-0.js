class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        const s_arr = s.split('').sort();
        const t_arr = t.split('').sort(); 

        return s_arr.join('') === t_arr.join('');
    }
}
