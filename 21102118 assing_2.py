


print('ANS 1')
rishi_str='Python is a case sensitive language'
print(len(rishi_str))
print( rishi_str[::-1])
s1=rishi_str[10:26]
print(s1)
s2=rishi_str[0:10],rishi_str[27:]
index=rishi_str.find("a")
print( index)
s3=rishi_str.replace(' ', '')
print( s3)

#Quesn.2
print('ANS 2')
Name=input('\nYour name:\n')
SID=int(input('\nYour SID:\n'))
Dep_name=input('\nYour Department name:\n')
CGPA=float(input('\nYour CGPA:\n'))
print('Hey, {s} Here!'.format(s=Name))
print('My SID is {d}'.format(d=SID))
print('I am from {s} department and my CGPA is {f}'.format(s=Dep_name,f=CGPA))

#QUES3
print('ANS 3')
a=56
b=10
print('\n(a) a&b =', a&b)
print('\n(b) a|b =', a|b)
print('\n(c) a^b =', a^b)
print('\n(d)')
print('After left shift by 2-bits, a =', a<<2)
print('After left shift by 2-bits, b =', b<<2)
print('\n(e)')
print('After right shift by 2-bits, a=', a>>2)
print('After right shift by 4-bits, b=',b>>4)

#Quesn.4
print ('Ans 4')
def isWordPresent(sentence, word ):
    s = sentence.split(" ")
    for i in s:
        if (i == word):
            return True
    return False
B = input('Enter the sentence/string -\n')
word ='name'
if word in B:
    print('\nYes')
else:
    print('\nNo')

#Quesn.5
print('Ans 5')
L1 = int(input('\nEnter the 1st length:\n'))
L2 = int(input('\nEnter the 2nd length:\n'))
L3 = int(input('\nEnter the 3rd length:\n'))
if L1>(L2+L3) or L2>(L1+L2) or L3>(L1+L2):
    print('\n No,entered three lengths can not form a triangle')
else:
    print('\n Yes,entered three lengths can form a triangle')

#Quesn.6
print('Ans6')
def countFlips(a, b):
    flips = 0
    while(a > 0 or b > 0):
      t1 = (a & 1)
      t2 = (b & 1)                                     
      if(t1 != t2):
            flips += 1
      a>>=1
      b>>=1
    return flips
a = int(input('enter value of a:\n'))
b = int(input('enter value of b:\n'))
print(countFlips(a, b))
 

    









