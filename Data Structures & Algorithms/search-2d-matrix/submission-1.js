class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let t = 0, b = matrix.length-1, l = 0, r = matrix[0].length-1;
        let row = null
        while (t <= b){
            const mid = Math.floor((t+b)/2)

            if(matrix[mid][0] > target){
                b = mid - 1
            } else if (matrix[mid][matrix[0].length-1] < target){
                t = mid + 1
            } else {
                row = mid
                break
            }
        }

        if(row === null) return false

        while (l <= r){
            const mid = Math.floor((l+r)/2)

            if (matrix[row][mid] < target){
                l = mid+1
            } else if (matrix[row][mid] > target){
                r =  mid - 1
            } else {
                return true
            }
        }
        return false
    }
}
