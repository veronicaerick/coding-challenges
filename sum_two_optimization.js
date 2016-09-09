// Question: From a unsorted array, check whether there are any two numbers that will sum up to a given number?

// naive brute force O(n2)

function sumTwo(arr, target) {

    var len = arr.length
    for (var i = 0; i < len; i++) {
        for (var j = 0; j < len; j++) {
            if arr[i] + arr[j] == target {
                return true;
            }
        }
    }
}

// optimze
// store differences of the sum and current element 
// for every element check to see if the diff is in object

function sumFinderV2(arr, target) {
    var diff = {};
    var len = arr.length;
    var sub;

    for (var i = 0; i < len; i++) {
        sub = target - arr[i];

        if diff[sub] {
            return true;
        } else {
            diff[arr[i]] == true;
        }
    }
}