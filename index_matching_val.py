# Given an array of sorted distinct integers named arr, write a function that returns an index i in arr for which arr[i] = i or -1 if no such index exists.

# Implement the most efficient solution possible, prove the correctness of your solution and analyze its runtime complexity (in terms of n - the length of arr).

# naive solution, runtime O(n)
def index_is_val(arr):
   for i, j in enumerate(arr):
      if i == j:
         return i

# optimized, O(n log n)
def index_is_val_search(arr):
   start = 0
   end = len(arr) - 1
   while (start <= end):
      i = (start+end)/2
      if (arr[i] - i < 0):
         start = i + 1
      elif (arr[i] - i == 0):
         return i
      else:
          end = i - 1

index_is_val_search([-1, 0, 2, 4])