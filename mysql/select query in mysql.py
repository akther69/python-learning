#select query in mysql

#COMPLETE SELECTION
# sql=select* from table_name

#selection using where clause
#slection usind id
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="employeee_management")
# mycursor=db.cursor()
# id=int(input("Enter the id="))
# sql="select * from employee_details where id=%d"%id
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print("id:",data[0])
# print("Employee name:", data[1])
# print("Email:", data[2])
# print("Phone:", data[3])


# select student detail using department
import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
mycursor=db.cursor()
department=input("Enter the department=")
sql="select * from student_details where department='%s'"%department
mycursor.execute(sql)
data=mycursor.fetchall()
for i in data:
    print("id:",i[0])
    print("student name:", i[1])
    print("school name:", i[2])
    print("department:", i[3])
    print("maths mark:", i[4])
    print("physics mark:", i[5])
    print("chemistry mark:", i[6])
    print()
