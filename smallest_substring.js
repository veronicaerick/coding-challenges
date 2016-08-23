function smallestSubstring(arr, str) {
    if(!arr && ! str)
        return;

    let charCheck = {};

    for index in arr
        charCheck[index] = true;

    for(let inx=0; idx <str.length -(arrayLength); idx++) {
        if(str[idx] == charCheck[str[idx]]) {
            charCheck[str[idx]] += 1;
        }
    }


function pramp() {
   console.log("Practice Makes Perfect");
}

pramp();


function smallestSubstring(arr, str){
   if(!arr  && !str)
      return; 
   
   // loop the string
   let characterCheck = {}; 
   
   for index in arr
      characterCheck[index] = 0;
   
   
   let arrayLength = arr.length;
   
   for(let idx = 0; idx < str.length- (arrayLength); idx++) {
      let head = arr[idx]; 
      let middle = arr[idx + 1];
      let tail = arr[idx + 2];
      
      
     if(head == characterCheck[head]){
         characterCheck[str[idx]] += 1;   
     }
     
     if(middle == characterCheck[middle]){
         characterCheck[str[idx]] += 1;   
     }
       
     if(tail == characterCheck[tail]){
         characterCheck[str[idx]] += 1;   
      }
      
     
   }
   
   
  xyy 
}

function getShortestUniqueSubstring(arr, str):
   t = 0
   result = null
   uniqueCounter = 0
   countMap = new Map()
   # initialize countMap:
   for i from 0 to length(arr)-1:
      countMap.setValueOf(arr[i], 0)
   # scan str
   for h from 0 to length(str)-1:
      # handle the new head
      head = str.charAt(h)
      if countMap.keyExists(head) == false:
         continue
      headCount = countMap.getValueOf(head)
      if headCount == 0: 
         uniqueCounter = uniqueCounter + 1
      countMap.setValueOf(head, headCount + 1)   
      # push tail forward
      while uniqueCounter == length(arr):
         tempLength = h - t + 1
         if tempLength == arr.length:
            return str.substring(t, h)
         if (!result or tempLength < length(result)):
            result = str.substring(t, h)
         tail = str.charAt(t) 
         if countMap.keyExists(tail):
            tailCount = countMap.getValueOf(tail) - 1
            if tailCount == 0:
               uniqueCounter = uniqueCounter - 1
            countMap.setValueFor(tail, tailCount)
         t = t + 1
   return result

t = 0
result: null
 uniqueChaacer = 0 -> 1-> 2 

headCount: 0
tempLenght=  3 

{
   x ==> 0--> 1 
   y ==> 0-->1
   z ==> 0
   
}

head - x