import sys

while True:
   Input=list(map(int, sys.stdin.readline().strip().split()))
   Input.sort()
   InputLength=len(Input)
   
   if InputLength == 1:
      break
   if Input[0] == 0:
      break

   #trial = 0
   s=1<<32
   values={}   
   for i in range(InputLength-1):
     for j in range(i+1,InputLength):
       newValue=Input[i]+Input[j]   
       if newValue>=s:
          continue
       elif newValue in values:
          s=newValue
          #trial += 1
       else:
          values[newValue]=True
   if s<1<<32:
      print ("yes: %d" %s)
   else:
      print ("None")
