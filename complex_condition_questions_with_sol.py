"""

41. Check whether a number is divisible by 5 and 11. 

num = int(input("Enter the number: "))
if num%5==0 and num%11!=0:
    print(f"{num} is not divisible by 11")
else:
    if num%5!=0 and num%11==0:
        print(f"{num} is not divisible by 5")
    else:
        print(f"{num} is divisible by 5 and 11")

------------------------------------------------------------------

42. Check if a person is eligible for loan: 
● age ≥ 21 
● salary ≥ 25,000 
● credit score ≥ 700

a = int(input("Enter the age: "))
b = int(input("Enter the salary: "))
c = int(input("Enter the credit score: "))
if a>=21 and b>=25000 and c>=700:
    print("You are eligible for loan")
else:
    print("You are not eligible for loan")

--------------------------------------------------------------

43. Validate login using username AND password. 

username = "Sanjeevk"
password = "Sanjeev123"
entered_username = input("Enter the username: ")
entered_password = input("Enter the password: ")
if entered_username!=username and entered_password==password:
    print("username is incoorect!")
else:
    if entered_username==username and entered_password!=password:
        print("password is incorrect!")
    else:
        print("You are logged in")

-----------------------------------------------------------------

44. Check student pass condition: 
● All subjects ≥ 40 
● Average ≥ 50

a = int(input("Enter math marks: "))
b = int(input("Enter english marks: "))
c = int(input("Enter history marks: "))
d = int(input("Enter hindi marks: "))
sum = a+b+c+d
average = sum/4
if a>=40 and b>=40 and c>=40 and d>=40 and average>=50:
    print(f"your average score is {average}\nResult: Pass")
else:
    print(f"Your average score is {average}\nResult: Fail")

----------------------------------------------------------------------

45. Check if a number lies between 10 and 100.

num = int(input("Enter the number: "))
if num>10 and num<100:
    print(f"{num} lies between 10 and 100")
else:
    print(f"{num} does not lie between 10 and 100")

----------------------------------------------------------------
 
46. Check exam eligibility: 
● attendance ≥ 75% OR 
● medical certificate available

att = int(input("Enter the attendance: "))
if att>=75:
    print(f"your attendance is {att}%\nYou can download your medical certificate")
else:
    print(f"your attendance is {att}%\nYour medical certificate is not available")

--------------------------------------------------------------------------------------

47. Validate a date using conditions.

date = int(input("Enter the date: "))
if date>=1 and date<=31:
    print(f"date {date} exists")
else:
    print(f"date {date} does not exist!")

------------------------------------------------------------

48. Check whether an email format is valid. 

greeting = "Hi, Sanjeev"
body_paragraph_1 = "My name is Sanjeev kumar"
body_paragraph_2 = "I am learning Data Science"
closing = "Thanks for reading my Email"
sign_off = "Sincerely,Sanjeev kumar"
a = input("write greetings: ")
b = input("write body_paragraph_1: ")
c = input("write body_paragraph_2: ")
d = input("write closing: ")
e = input("write sign_off: ")
if a==greeting and b==body_paragraph_1 and c==body_paragraph_2 and d==closing and e==sign_off:
    print("Email format is valid")
else:
    print("Email format is not valid !")

---------------------------------------------------------------------

49. Determine insurance eligibility using age, health status, and income. 

age = int(input("Enter the age: "))
sal = int(input("Enter the salary: "))
health = input("Enter the health status: ")
if age>=18 and age<=50 and sal>=50000 and sal<=80000 and health in "GoodgoodNiceniceAwesomeawesome":
    print(f"Your condition is {health}\nIt is not needed to claim for hearlth insurance")
else:
    print(f"Your condition is {health}\nYou are advised to claim for hearlth insurance")

-------------------------------------------------------------------------------------------------

50. Check leap year using complete leap year logic. 


"""
year = int(input("Enter the year: "))
if year%4==0 and year%100!=0:
    print(f"{year} is a leap year")
else:
    if year%4==0 and year%400==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")