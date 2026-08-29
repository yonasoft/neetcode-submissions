class LLNode {
    constructor(val = null, next = null) {
        this.val = val
        this.next = next
    }
}

class LinkedList {
    constructor() {
        this.head = new LLNode(-1)
        this.tail = this.head
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let curr = this.head.next;
        let i = 0;
        while(curr){
            if(i === index){
                return curr.val
            }
            curr = curr.next;
            i++;
        }
        return -1
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let newNode = new LLNode(val)
        newNode.next = this.head.next
        this.head.next = newNode
        if(!newNode.next){
            this.tail = newNode
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let newNode = new LLNode(val)
        this.tail.next = newNode
        this.tail = newNode
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let curr = this.head;
        while (i < index && curr) {
            i++;
            curr = curr.next;
        }

        // Remove the node ahead of curr
        if (curr && curr.next) {
            if (curr.next === this.tail) {
                this.tail = curr;
            }
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let res = [];
        let curr = this.head.next;
        while(curr){
            res.push(curr.val);
            curr = curr.next;
        }
        return res;
    }
}
