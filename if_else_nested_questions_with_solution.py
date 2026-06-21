"""

21. Find the largest of three numbers. 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a>b and a>c:
    print(f"{a} is greater among the numbers.")
else:
    if b>c:
        print(f"{b} is greater among the numbers.")
    else:
        print(f"{c} is greater among the numbers.")

----------------------------------------------------------------------------

22. Check whether a number is positive, negative, or zero.

num = int(input("Enter the number:"))
if num>0:
    print(f"{num} is a Positive number.")
else:
    if num<0:
        print(f"{num} is a Negative number.")
    else:
        print(f"You entered {num} which is a Whole number.")

-----------------------------------------------------------------------------

22. Check whether a number is positive, negative, or zero. 
23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60 

marks = int(input("Enter your marks:"))
if marks>=90:
    print(f"Your marks is {marks}\nYou got grade:A")
else:
    if marks>=75 and marks<90:
        print(f"Your marks is {marks}\nYou got grade:B")
    else:
        if marks>=60 and marks<75:
            print(f"Your marks is {marks}\nYou got grade:C")
        else:
            print(f"Your marks is {marks}\nFail,Better luck next time!")

--------------------------------------------------------------------------------

24. Check whether a triangle is equilateral, isosceles, or scalene. 

side_a = int(input("Enter the side_a:"))    #All sides should be same for Equilateral Triangle
side_b = int(input("Enter the side_b:"))    #Any two sides should be same for Isosceles Trianle
side_c = int(input("Enter the side_c:"))    #All sides should be different for Scalen Triangle
if side_a==side_b==side_c:
    print("It is Equilateral Triangle")
else:
    if side_a==side_b or side_b==side_c or side_c==side_a:
        print("It is Isosceles Triangle")
    else:
        print("It is Scalen Triangle")

----------------------------------------------------------------------------------

25. Check whether a character is uppercase, lowercase, digit, or special character. 

ch = input("Enter a character: ")

if "A"<=ch<="Z":
    print(f"{ch} is uppercase")
else:
    if "a"<=ch<="z":
        print(f"{ch} is lowercase")
    else:
        if "0"<=ch<="9":
            print(f"{ch} is digit")
        else:
            print(f"{ch} is special symble")

----------------------------------------------------------------------------------

27. Validate login using username and password. 

username = "Sanjeevk"
passwrod = "Sanjeev123"
enter_username = input("Enter the username:")
enter_password = input("Enter the password:")
if enter_username!=username and enter_password==passwrod:
    print(f"Username is wrong!")
else:
    if enter_username==username and enter_password!=passwrod:
        print(f"Password is wrong!")
    else:
        print(f"You are logged in.")

---------------------------------------------------------------------------

26. Calculate electricity bill using slab-wise rates. 

bill = int(input("Enter the bill amount:"))
rate_1 = 2.5
rate_2 = 5
rate_3 = 7.5
rate_4 = 10
if bill>=4000 and bill<=4500:
    print(f"Your bill amount is {bill} plus GST {rate_1}%\nYour total payment is {bill*1.025}")
else:
    if bill>4500 and bill<=5000:
        print(f"Your bill amount is {bill} plus GST {rate_2}%\nYour total payment is {bill*1.05}")
    else:
        if bill>5000 and bill<=6000:
            print(f"Your bill amount is {bill} plus GST {rate_3}%\nYour total payment is {bill*1.075}")
        else:
            print(f"Your bill amount is {bill} plus GST {rate_4}%\nYour total payment is {bill*1.1}")

-----------------------------------------------------------------------------------------------------------

28. Check student result using marks of 3 subjects. 

a = int(input("Enter your English marks:"))
b = int(input("Enter your Math marks:"))
c = int(input("Enter your Acoount marks:"))
sum = a+b+c
average = sum/3
if average>=35:
    print(f"English:{a}\nMath:{b}\nAccount:{c}\nYour total marks is : {sum}\nYour percentage is : {average}\nResult : Pass")
else:
    print(f"English:{a}\nMath:{b}\nAccount{c}\nYour total marks is : {sum}\nYour percentage is : {average}\nResult : Fail")

------------------------------------------------------------------------------------------------------------

29. Find the second largest number among three numbers. 

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a>b and a>c:
    print(f"{a} is largest among all")
else:
    if b>c:
        print(f"{b} is second largest among all")
    else:
        print(f"You entered third number {c} which is wrong because {c} should be smaller")

-------------------------------------------------------------------------------------------------

30. Check loan eligibility using age, salary, and credit score. 
"""
sal = float(input("Enter the salary in LPA:"))
age = int(input("Enter the age:"))
credit_score = float(input("Enter the credit score:"))
if sal>=8 and age>=18 and credit_score>=7 and credit_score<=10:
    print("You are eligible for Loan")
else:
    print("You are not eligible for Loan!")