

function smallestSubstr(arr, str) {
    arrLen= arr.length
    // min length of substring should be the arrays len
    let lenOfSubstr = arrLen;
    let strLen = str.length;
    let startIdx = 0;
    let subStr;
    let match; 
    // see if substring has all chars from arr
    let i;
    let val;
    // the max lengeth of substring should be smaller than
    // the strings lengeth
    while (lenOfSubstr <= strLen) {
        subStr = str.substr(startIdx, lenOfSubstr);
    if (subStr.length === lenOfSubstr) {
        match = true;
        // check if substring have all chars of the given array
        for (var i = 0; i < arrLen; i ++) {
            val = arr[i];
            if (subStr.indexOf(val) == -1) {
                match = false;
                break;
            }
        }
        if (match) {
            return subStr;
        }
        startIdx ++;
    } else {
        startIdx = 0;
        lenOfSubstr++;
    }
    }
    return null;
}