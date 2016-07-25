function checkPalindrome(word) {    
    var len = word.length;
    for (var i = 0; i < len / 2; i++) {
        if (word.charAt(i) !== word.charAt(l - 1 - i)) {
            return false;
        }
    }
    return true;
}

