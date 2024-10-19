#question 3
# >=18 <30 m 700 f 750
# >=30 <=40 m 800 f 850
gender=input("Enter the gender = ").upper()
age=int(input("Enter the age = "))
day=int(input("Enter the number of days worked = "))
if(age>=18 and age<30):
    if(gender=="M"):
        wage=day*700
        print("the wage is",wage)
    elif(gender=="F"):
        wage = day * 750
        print("the wage is", wage)
elif(age>=30 and age<=40):
    if(gender=="M"):
        wage=day*800
        print("the wage is",wage)
    elif(gender=="F"):
        wage = day * 850
        print("the wage is", wage)
else:
    print("no wage")
