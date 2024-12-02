#reconstructSentence.py 
#this program reconstrocts a sentence from two input text files
#which have been revesed and devided in two
#exaple: python3 reconstructSentence.py ./input1.txt ./input2.txt
#made by Shawn Farnham on 12-2-2024

import sys

def splitter(text_name):
  w=text_name.split()
  return w

def flip(list):
  temp = []
  for k in range(len(list)):
    temp.append(list[-1])
    del list[-1]
  return temp
  

infile1 = open(sys.argv[1])
infile2 = open(sys.argv[2])
output=[]

text1=infile1.readlines()
text2=infile2.readlines()
print("text1 is: ", text1)
print("text2 is: ", text2)

text1s = text1[0].split()
text2s = splitter(text2[0])

text1sr= flip(text1s)
text2sr= flip(text2s)

for l in range(len(text1sr)):
  output.append(text1sr[l])
  if l < len(text2sr):
    output.append(text2sr[l])

print("output is: ", output)
my_output=" ".join(output)

fp = open("output.txt", "w")
fp.write(my_output)
fp.close()
