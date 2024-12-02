#sumLines.py
#this program reads a text file and calculates the sum, number of integers, and
#average of the numbers
#example usage: python3 sumLines.py ./dataInput.txt
#made by Shawn Farnham on 12-2-2024

import sys

list=[]
countNum = 0
sum = 0
mean = 0

file= open(sys.argv[1])
flines = file.readlines()
linecount = len(flines)
for i in flines:
  w=i.split()
  for j in range(len(w)):
    list.append(int(w[j]))
    countNum += 1

for x in range(countNum):
  sum = sum + list[x]
 
mean = sum/countNum

print("Count: ", countNum)
print("Sum: ", sum)
print("Mean: ", mean)

