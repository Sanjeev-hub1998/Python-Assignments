"""

31. Print day name using day number (1-7). 

num = int(input("Enter the number from 1 to 7 :"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Satuday")
else:
    if num==7:
        print("Sunday")

------------------------------------------------

32. Print month name using month number. 

num = int(input("Enter the month number from 1 to 12 :"))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
else:
    if num==12:
        print("December")
    else:
        print("Data not found!")

--------------------------------------------------------

33. Display grade based on percentage. 

per = float(input("Enter the percentage:"))
if per>=90:
    print(f"Your percentage is {per}\ngrade:A")
elif per>=75 and per<90:
    print(f"Your percentage is {per}\ngrade:B")
elif per>=60 and per<75:
    print(f"Your percentage is {per}\ngrade:C")
else:
    print(f"Your percentage is {per}\ngrade:D")

--------------------------------------------------------

34. Display bonus percentage based on experience years. 

year = int(input("Enter experience in years: "))
if year==1:
    print(f"You have {year} years experience so your bonus is 3%")
elif year>1 and year<=5:
    print(f"You have {year} years experience so your bonus is 12%")
elif year>5 and year<=10:
    print(f"You have {year} years experience so your bonus is 20%")
else:
    print(f"You have {year} years experience so your bonus is 40%")

---------------------------------------------------------------------

35. Identify traffic signal meaning. 

light = input("Enter the light color: ")
if light=="red":
    print("Stop!")
elif light=="yello":
    print("Walk")
elif light=="green":
    print("Go")
else:
    print("Light is broken!")

-----------------------------------------------

36. Categorize temperature as Cold / Warm / Hot. 

tem = int(input("Enter the temperature: "))
if tem>=32:
    print("Hot")
elif tem>=15 and tem<32:
    print("Warm")
else:
    print("Cold")

------------------------------------------------------

37. Categorize employee based on salary range. 

sal = int(input("Enter the salary in LPA: "))
if sal<=3:
    print("Data Operator")
elif sal<=6 and sal>3:
    print("Accountant")
elif sal<=10 and sal>6:
    print("Data Analyst")
elif sal<=15 and sal>10:
    print("HR")
else:
    print("Data Scientist")

---------------------------------------------------------

38. Print discount percentage based on purchase amount. 

pur = int(input("Enter the purchased amount: "))
if pur>=1000 and pur<2000:
    print(f"You have purchased the items of {pur}rs ,You got the discount of 5%")
elif pur>=2000 and pur<3500:
    print(f"You have purchased the items of {pur}rs ,You got the discount of 10%")
elif pur>=3500 and pur<5000:
    print(f"You have purchased the items of {pur}rs ,You got the discount of 15%")
else:
    print(f"You have purchased the items of {pur}rs ,You got the discount of 20%")

-----------------------------------------------------------------------------------------

39. Identify number type: single-digit / double-digit / multi-digit. 

num = int(input("Enter the number: "))             # Number should be greater than or equal to 0
if num>=0 and num<=9:
    print(f"{num} is a single-digit number")
elif num>=10 and num<=99:
    print(f"{num} is double-digit number")
else:
    print(f"{num} is multi-digit number")

-----------------------------------------------------------------

40. Assign performance rating: Poor / Average / Good / Excellent. 

"""
marks = float(input("Enter the marks: "))
if marks>=90:
    print("Excellent Performance")
elif marks>=75 and marks<90:
    print("Good Performance")
elif marks>=50 and marks<75:
    print("Average Performance")
elif marks>=35 and marks<50:
    print("Poor Performance")
else:
    print("Fail")
