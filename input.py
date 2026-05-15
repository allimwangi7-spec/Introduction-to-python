"""

using input to prompt user enter values
-It uses to enter his/her name and displays the name on console window
(1)Input() function allows one to input value, the computer converts them to readable format

Example
Name=Input("Enter your name")
This allows user to input the name.

(2)Age=Int(input("Enter age"))
-Age is an integer, it must be converted to integer firts by
Age=Int()

"""

student_name=input("Enter your name ")
age=int(input("Enter your age "))
print(f" Hello  {student_name}, you are {age} years old ")