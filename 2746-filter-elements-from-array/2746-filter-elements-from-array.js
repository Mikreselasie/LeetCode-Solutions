/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let my_arr = [];
    for(let i = 0; i<arr.length; i++){
        if(fn(arr[i],i)){
            my_arr.push(arr[i]);
        }
    }
    return my_arr
};