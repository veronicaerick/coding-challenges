function letterCounter(string):

  var words= string.split(" ");
  var dict = {}
  // loop through each word
  for (var i = 0; i < words.length; i ++) {
    var thisWord = words[i];
    dict[thisWord] = {};

    // create a key/value pair that will store
    // the highest letter count for each word
    dict[thisWord]["highest"] = 0;

    // loop through each character in word and
    // store number of times each letter appears
    for (var count = 0; count  < words[i].length; count ++) {
      // does this char exist in dict, if so add count. if not
      // start count at 1
      var thisChar = thisWord[count];
      dict[thisWord][thisChar] = undefined ?
        dict[thisWord][thisChar] = 1;
        dict[thisWord][thisChar] += 1;

        // update the highest letter count for each new letter
        if (dict[thisWord][thisChar] > dict[thisWord][thisChar]["highest"]) {
          dict[thisWord]["highest"] = dict[thisWord][thisChar];
        }
    }

  }

  var result = {word: null, count:1};

  for (var w in dict) {
    if (dict[w]["highest"] > result["count"]) {
      result["count"] = dict[w]["highest"];
      result["word"] = w;
    }
  }

  return (result["count"] == 1) ? -1 : result["word"];

/////////////////////////////////////////////////////
function letterCounterv2(str) {
  var words = str.split(" ");
  var longestWord = "";
  var longestWordLength = 0;
  // for each letter, start a count or add count by 1 if already there
  for (var i = 0; i < words.length; i++) {
    var dict = {};
    var word = words[i];
    for (w of word) {
      if (dict[w] == undefined)
          dict[w] = 0;
        dict[w]++;
    }
    // for each w in dict, find max length. if max is longer than
    // currently assigned word, reassign. 
    maxLen = 0
    for (w in dict)
      maxLen = Math.max(maxLen, dict[w]);
    if (maxLen > longestWordLength)
      longestWordLength = maxLen;
      longestWord = word;

  }
}
  if (longestWordLength == 1)
    return "-1"
  return longestWord;
}
