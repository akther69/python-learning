#mysql delete
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="employeee_management")
# mycursor=db.cursor()
# data="select id from employee_details"
# mycursor.execute(data)
# fetch=mycursor.fetchall()
#
# id=int(input("Enter the id to delete="))
# for i in fetch:
#     if(id==i[0]):
#         sql="delete from employee_details where id=%d"%id
#         mycursor.execute(sql)
#         db.commit()
#         print("The deletion is executed successfully")
#         break
# else:
#     print("Please enter the valid id")


#task
#write sql query to delete student details using student name
import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
mycursor=db.cursor()
data="select studentname from student_details"
mycursor.execute(data)
fetch=mycursor.fetchall()

studentname=input("Enter the student name to delete=")
for i in fetch:
    if(studentname==i[0]):
        sql="delete from student_details where studentname='%s'"%studentname
        mycursor.execute(sql)
        db.commit()
        print("The deletion is executed successfully")
        break
else:
    print("Please enter the valid studentname")