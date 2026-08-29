class Solution {
    /**
     * @param {number} prices
     * @return {number}
     */
    maxProfit(prices) {
        let curr_min = prices[0]
        let max_profit = 0

        for(const p of prices){
            curr_min = Math.min(curr_min, p)
            max_profit = Math.max(max_profit, p-curr_min)
        }

        return max_profit
    }
}
