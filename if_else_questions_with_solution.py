"""
11. Check whether a number is even or odd.

num = int(input("Enter the number:"))
if num%2==0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")
---------------------------------------------------------------

12. Find the largest of two numbers.

num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
if num_1>num_2:
    print(f"{num_1} is greater than {num_2}")
else:
    print(f"{num_2} is greater than {num_1}")
---------------------------------------------------------------

13. Check whether a person is eligible for driving license.

age = int(input("Enter the age:"))
if age>=18:
    print(f"You are {age} years old.You are eligible for driving.")
else:
    print(f"You are {age} years old.You are not eligible for driving.")

----------------------------------------------------------------------

14. Print "Pass" or "Fail" based on marks. 

marks = int(input("Enter your marks:"))
if marks>=35:
    print(f"Pass")
else:
    print(f"Fail")

-------------------------------------------------------------------------

15. Check whether a number is positive or negative. 

print("You can enter any intiger number except 0 because it is a whole number.")
num = int(input("Enter the number:"))
if num>0:
    print(f"{num} is a Positive number")
else:
    print(f"{num} is a negative number")

--------------------------------------------------------------------------

16. Check whether a character is a vowel or consonant. 

ch = input("Enter the character:")
if ch in "AEIOUaeiou":
    print(f"{ch} is Vowel")
else:
    print(f"{ch} is Consonant")

----------------------------------------------------------------------------

17. Check if a year is leap or not.



---------------------------------------------------------------------------

18. Print "Valid Password" or "Invalid Password". 

password = "Sanjeev123"
entered_password = input("Enter the password:")
if entered_password==password:
    print("Valid password!")
else:
    print("Invalid password!!")

---------------------------------------------------------------------------

19. Determine whether salary is taxable or not.

sal = int(input("Enter your salary:"))
if sal>1200000:
    print(f"Your salary is {sal} which is above limit.Your salary is taxable.")
else:
    print(f"Your salary is {sal} which is under limit.Your salary is not taxable.")

--------------------------------------------------------------------------

20. Check whether a number is greater than 50 or not.

num = int(input("Enter the number:"))
if num>50:
    print(f"{num} is greater than 50")
else:
    if num==50:
        print(f"Your number is 50")
    else:
        print(f"{num} is less than 50")

----------------------------------------------------------------------------
"""
year = int(input("Enter the year:"))
if year%4==0 and year%100!=0:
    print(f"{year} is a leap year")
else:
    if year%4==0 and year%400==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
