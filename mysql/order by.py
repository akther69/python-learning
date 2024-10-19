#ORDER BY
#ascending order
# select * from table name order by name
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="employeee_management")
# mycursor=db.cursor()
# sql="select * from employee_details order by name desc"
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     print("Name=",i[1])


#select studentname and maths score from student detail table
#select option:
#high-low mark
#low high mark
#enter the option:1
import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
mycursor=db.cursor()
print("Select the option 1 or 2")
print("if 1:Low-High mark")
print("if 2:High-Low mark")
option=int(input("Enter the option="))
if(option==1):
    sql="select * from student_details order by maths_score"
elif(option==2):
    sql = "select * from student_details order by maths_score desc"
mycursor.execute(sql)
data=mycursor.fetchall()
for i in data:
    print("Name=",i[1]) #here all the table is called so it i[1]  and i[4]
    print("Maths Score=",i[4])
    print()

    #and above it call only specific table