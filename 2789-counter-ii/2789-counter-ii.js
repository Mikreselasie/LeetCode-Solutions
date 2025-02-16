/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let x = init;
    function increment(){
        x += 1;
        return x;
    }
    function decrement(){
        x -= 1;
        return x;
    }
    function reset(){
        x = init;
        return x ;
    }
    return {increment,decrement,reset}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */