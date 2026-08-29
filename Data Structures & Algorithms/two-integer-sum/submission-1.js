class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const visited = new Map()
        for (const [i, n] of nums.entries()){
            const difference = target - n
            if (visited.has(difference)){
                return [visited.get(difference), i]
            }
            visited.set(n, i)
        }
    }
}
        
