
def timePlanner(timesA, timesB, dur):
  timesA = sorted(timesA)
  timesB = sorted(timesB)
  i = 0 
  j = 0
  while (i < len(timesA) and  j < len(timesB)):
    d = len(set(range(timesA[i][0], timesA[i][1])).intersection(range(timesB[j][0], timesB[j][1])) )
    if d >= dur:
      return True
    
    if timesA[i][1] < timesB[j][1]:
      i += 1
    else:
      j += 1

  return False
 

# test 
A = [[0,3], [4,6], [8,9]]
B = [[4,5], [6,8], [0,2]]
dur = 2
print(timePlanner(A,B,dur))