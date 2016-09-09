import pdb

"""
Run this script to run testcases for the problem:
  $ python main.py
  [i=1] PASS. arr='['x', 'y', 'z']' str='xyyzyzyx' Out: zyx Truth: zyx
  [i=2] PASS. arr='['a']' str='aabc' Out: a Truth: a
  [i=3] PASS. arr='['a', 'b']' str='acbcaabc' Out: ab Truth: ab
  [i=4] PASS. arr='['a', 'b']' str='bccac' Out: bcca Truth: bcca

Problem:
Given an array with unique characters arr and a string str, find the
smallest substring of str containing all characters of arr.

Example:
arr: [x,y,z], str: xyyzyzyx
result: zyx
"""

def getShortestUniqueSubstring_ek(arr,str):
    """
    Brute-force solution.
    Runtime: O(n^2) substrings, each iter is O(m + n), where m is len(arr),
      n is len(str).
      O(n^2 * (m + n)) total (I think!)
    """
    # Calculate counts of chars in arr
    cnts_arr = calc_cnts(''.join(arr)) # ex: {'x': 1, 'y': 2, 'z': 1}
    # Check all possible substrings
    shortest = None # stores shortest satisfying substring
    for i1 in xrange(len(str)):
        for i2 in xrange(i1, len(str)):
            substr = str[i1:(i2+1)]
            cnts_substr = calc_cnts(substr)
            if cnts_satisfy(cnts_arr, cnts_substr):
                if shortest is None:
                    # First time we found a satisfying substring
                    shortest = substr
                elif len(substr) < len(shortest):
                    # We found a shorter satisfying substring
                    shortest = substr
    return shortest

def calculate_counts(s):
    """ Calculate character counts in string s.
    INPUT
      string chars:
    OUTPUT
      dict cnts:
    """
    cnts = {}
    for char in s:
        if char not in cnts:
            cnts[char] = 1
        else:
            cnts[char] += 1
    return cnts
    
def counts_satisfy(cnts1,cnts2):
    """ Return True if the characters in cnts1 are "covered" by the
    characters in cnts2, ie:
      cnts1[c] <= cnts2[c] for all c in cnts1
    INPUT
      dict cnts1:
      dict cnts2:
    OUTPUT
      bool is_satisfy:
    """
    for char,cnt in cnts1.iteritems():
        if (char not in cnts2) or (cnts2[char] < cnt):
            return False
    return True

def getShortestUniqueSubstring_pramp(arr, str):
   """
   Pramp's optimal answer, translated to Python.
   """
   t = 0
   result = None
   uniqueCounter = 0
   countMap = {}
   # initialize countMap:
   for i in xrange(len(arr)):
      countMap[arr[i]] = 0
   # scan str
   for h in xrange(len(str)):
      # handle the new head
      head = str[h]
      if head not in countMap:
         continue
      headCount = countMap[head]
      if headCount == 0:
         uniqueCounter = uniqueCounter + 1
      countMap[head] = headCount + 1
      # push tail forward
      while uniqueCounter == len(arr):
         tempLength = h - t + 1
         if tempLength == len(arr):
            return str[t:(h+1)]
            #return str.substring(t, h)
         if (not result) or (tempLength < len(result)):
            result = str[t:(h+1)] #.substring(t, h)
         tail = str[t]
         if tail in countMap:
            tailCount = countMap[tail] - 1
            if tailCount == 0:
               uniqueCounter = uniqueCounter - 1
            countMap[tail] = tailCount
         t = t + 1
   return result

def main():
    # (1) Define testcases, with expected input/output.
    testcases = [
        # [ <list arr>, <str str>, <str truth> ]
        [ ['x','y','z'], 'xyyzyzyx', 'zyx' ],
        [ ['a'], 'aabc', 'a' ],
        [ ['a', 'b'], 'acbcaabc', 'ab' ],
        [ ['a', 'b'], 'bccac', 'bcca' ],
    ]
    # (2) Run tests.
    for test_i, (arr,str,truth) in enumerate(testcases):
        arr = testcases[test_i][0]
        str = testcases[test_i][1]
        truth = testcases[test_i][2]
        
        #out = getShortestUniqueSubstring_ek(arr,str) # My brute-force solution
        out = getShortestUniqueSubstring_pramp(arr,str) # Pramp's solution
        status = ("PASS" if out == truth else "FAIL")
        print "[i={0}] {1}. arr='{2}' str='{3}' Out: {4} Truth: {5}".format(test_i+1,status,arr,str,out,truth)

if __name__ == '__main__':
    main()
