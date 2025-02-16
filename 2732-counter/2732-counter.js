/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let current = n - 1;
    return function() {
        current += 1;
       return current;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */