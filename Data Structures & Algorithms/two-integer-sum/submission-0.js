class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const visited = new Map()
        for (let i = 0; i < nums.length; i++){
            const n = nums[i]
            const difference = target-n
            if (visited.has(difference)){
                return [visited.get(difference), i]
            }
            visited.set(n, i)
        }
    }
}
