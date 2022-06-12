 #Quesn_1:
"""
M1 = float(input("Enter Your marks:"))
if M1 < 25:
    print("Your Grade is:- F ")
elif 25 <= M1 <45:
    print("Your Grade is:- E ")
elif 45 <= M1 <50:
    print("Your Grade is:- D ")
elif 50 <= M1 < 60:
    print("Your Grade is:- C ")
elif 60 <= M1 < 80:
    print("Your Grade is:- B ")
else:
    print("Your Grade is:- A ")
"""
#Quesn_2:
"""
Year = int(input("Enter the Year:"))
if Year % 4 == 0:
    print("A Leap Year.")
elif Year % 100 == 0:
    print("Not a Leap Year.")
elif Year % 400 == 0:
    print("A Leap Year.")
else:
    print("Not a Leap Year.")
"""
#Quesn_3:
"""
import random
for i in range(10):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print(f"Question {i+1}:",end="")
    user_output = int(input(f"{n1}X{n2}="))
    if user_output == (n1*n2):
        print("Right!")
    else:
        print(f"Wrong, The answer is {n1*n2}")
"""
#Quesn_4:
"""
x=200
for candies in range(x):
    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies,'Candies are there in the bowel.')
             break
"""