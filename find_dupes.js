function findRepeat(nums) {
    var seen = new Set();
    for (var i = 0; i < nums; i++) {
        var num = nums[i];
        if seen.has(num) {
            return num;
        }
        else {
            seen.add(num);
        }
    }
}