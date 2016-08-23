/*
 * Word Count Engine
 *
 * Implement a document scanning engine that receives a text document doc and
 * returns a list of all unique words in it and their number of occurrences,
 * sorted by the number of occurrences in descending order.
 *
 * Example:
 *   document = "practice makes perfect. get perfect by practice. just
 *   practice!";
 *
 *   // the engine returns the list: { practice: 3, perfect: 2,  makes: 1, get: *   1, by: 1, just: 1 }.
 *
 * The engine should ignore punctuation and white-spaces.
 * Find the minimal runtime complexity and analyze it.
 */


// get rid of punctuation, start a hashmap with word counts, pull out each key/val into an array, then sort by descending

var startEngine = document => {
    var wordCounts = []
}
 // remove all special characters using RegEx: /[^\w\s]/gi and /[_]/gi
  // split document by space and store into words array
var words = document.replace(/[^\w\s]/gi, '').replace(/[_]/gi, '').split(' ');
var len = words.length;
// create an empty hash
var dict = {};
var word = '';

// loop through all words
for (var w = 0; w < len; w ++) {
    // start count for each word
    word = words[w];
    if (dict.hasOwnProperty(word)) {
        // if word is in there, increment count
        dict[word]++;
    } else {
        // word isnt there, start count at 1
        dict[word] = 1;
    }
}
//  now that we have our dictionary, loop through and grab key value
// pairs push to list
var count;
for (var word in dict) {
    count = dict[word];
    wordCounts.push([word,count]);
}

// sort the words by cont
wordCounts.sort(count)

return wordCounts;
