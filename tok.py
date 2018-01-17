import re
                                                                                                                                                                     
f1 = open("input.txt","r")
o = open("operator.txt","r")
k = open("keywords.txt","r")
pu = open("pun.txt","r")
pun = pu.read()
inp = f1.read()
op = o.read()
key = k.read()
inr = re.split(r'(\d+|\W+)',inp)
opr = op.split()
punc = pun.split()
keyw = key.split()
idno = 0
print (inr)
for x in inr:
       if (x == ' ' or x =='\n' or x == ''):
               continue
       if x in opr:
               print ("Operator: ", x)
       elif x in punc:
               print ("Punctuation :", x)
       elif x in keyw:
               print ("Keyword: ", x)
       elif x.isdigit():
               print ("Number: ", x)
       else:
               print ("id",idno,": ", x)
               idno+=1
