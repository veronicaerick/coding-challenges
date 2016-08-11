function LongestWord(sen) {
  var lst = sen.match(/a-z0-9+/gi);
  var sorted = lst.sort(function(a,b)) {
    return b.length - a.length;
  });
  return sorted[0]
}
