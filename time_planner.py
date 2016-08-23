
def timePlanner(timesA, timesB, dur):
  A = sorted(timesA)
  B = sorted(timesB)
  i = 0 
  j = 0
  while (i < len(A) and  j < len(B)):
    d = len( set(range(A[i][0], A[i][1])).intersection(range(B[j][0], B[j][1])) )
    if d >= dur:
      return True
    
    if A[i][1] < B[j][1]:
      i += 1
    else:
      j += 1

  return False
 

# test 
A = [[0,3], [4,6], [8,9]]
B = [[4,5], [6,8], [0,2]]
dur = 2
print(timePlanner(A,B,dur))