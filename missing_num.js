function missingNum(arr) {
    var n = arr.length+1
    sum = 0;
    expectedSum = n * (n +1)/2;

    for (var i = 0; i < n; i++) {
        sum += arr[i];
    }
    return expectedSum - sum;
}

function missingNum(arr) {
    var len = arr.length + 1;
    var sum = 0;
    var expectedSum = len * (len +1)/2;

    for (var i; i < len; i++) {
        sum += i;

    }
    return expectedSum - sum;
}