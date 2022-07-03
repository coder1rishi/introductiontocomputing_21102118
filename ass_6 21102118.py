#qu.1
i = input("enter number :")
i = int(i)
Sum = 0

for e in range(1, i):
    if i % e == 0:
        Sum += e

if i == Sum:
    print(f"{Sum} is perfect number")
else:
    print("try another number")
#qu.2
n = input('enter string : ')
n = n.replace(' ', '')
if n == n[::-1]:
    print("palindrome")
else:
    print('try again')
#qu.3
I = [1, 1]
n = int(input("enter no. of row"))
print([1])
for _ in range(n):
    lst = []
    Sum = 0
    for e in range(0, len(I) - 1):
        Sum = I[e] + I[e + 1]
        lst.append(Sum)
    I = [1] + lst + [1]
    print(I)
#qu.4
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
#qu.5
i = input("enter your string : ")
i = i.replace(' ', '')
lst = set(i)
lst = list(lst)
#print(lst)

alphabets = 'qwertyuioplkjhgfdsazxcvbnm'
alphabets = list(alphabets)
#print(alphabets)


check = 0
for i in lst:
    if i in alphabets:
        check += 1


if check == len(alphabets):
    print('yes')
else:
    print('no')
#qu.6
class student_data:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def student_id(self):
        print(f'name : {self.name} ||| branch : {self.branch}')


s = student_data('rishhhhi', 'civil')
# function
s.student_id()

# arguments
print('--->', s.name)
print('--->', s.branch)
#qu.7
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
#qu.8
class py_solution:

   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))




