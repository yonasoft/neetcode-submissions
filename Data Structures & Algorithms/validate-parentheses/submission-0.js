class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []
        const pairs = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for (const c of s){
            if(!(c in pairs)){
                stack.push(c)
                continue
            } else {
                if(stack[stack.length-1] === pairs[c]){
                    stack.pop()
                    continue
                }
            }

            return false
        }

        return stack.length === 0
    }
}
