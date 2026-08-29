class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {

        this.capacity = capacity;
        this.arr = new Array(this.capacity).fill(0);
        this.size = 0;
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.arr[i];
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.arr[i] = n;
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if(this.size === this.capacity){
            this.resize();
        }
        this.arr[this.size] = n;
        this.size+=1;
    }

    /**
     * @returns {number}
     */
    popback() {
        if( this.size > 0 ){
            this.size-=1;
        }
        return this.arr[this.size];
    }

    /**
     * @returns {void}
     */
    resize() {
        const newArr = [...this.arr, ...Array(this.capacity).fill(0)];
        this.arr = newArr;
        this.capacity*=2;
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.size;
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity;
    }
}
