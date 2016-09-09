def smallestSubstring(arr, s):
   #arr is a List[char]
   #s is a string
   #return type is a string
   
   #We can eliminate null arrays immediately as a base case
   if not arr: return ""
   
   #The string we will be appending to
   res = ""
   container_dict = createDictionary(arr)
   i = j = 0
   size = len(arr)
   while i < size:
      while j < size:
         container_dict[arr[j]] -= 1
         if container_dict[arr[j]] < 0:
            #Reset
            res = ""
            j += 1
            i = j
            #Reset the dictionary
            container_dict = createDictionary(arr)
            break
         else:
            res += arr[j]
            j += 1
   return res
def createDictionary(arr):
   #arr is List[char]
   #return dictionary
   container_dict = {} #empty dictionary we shall fill
   #Loop through all the characters in the array
   for char in arr:
      #if the character does not exist as a key in the dictionary
      if not container_dict.get(char, 0):
         #Add it and initialize its value to 1
         container_dict[char] = 1
      else:
         #If it already exists, we simply increment the count
         container_dict[char] += 1
   return container_dict    

# It's your peer's turn to interview you:  The question you are asked is in the left pane below the video
# The stream was unable to connect due to a network error. Make sure your connection isn't blocked by a firewall.
# Mute
# The "Shifted Array Search" Problem

# 1. Find a given number num in a sorted array arr:
# arr = [2, 4, 5, 9, 12, 17] 

# 2. If the sorted array arr is shifted left by an unknown offset and you don't have a pre-shifted copy of it, how would you modify your method to find a number in the shifted array?
# shiftArr = [9, 12, 17, 2, 4, 5]

# Explain and code an efficient solution and analyze its runtime complexity
# if num doesn't exist in the array, return -1