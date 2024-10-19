#select detail using coloumn name
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="employeee_management")
# mycursor=db.cursor()
# sql="select name,email from employee_details"
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     print("Employee Name=",i[0])
#     print("Employee email=",i[1])
#     print()


#select student name maths,phys,chem score pf a particular student using their name input by the user
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# name=input("Enter the name=")
# sql="select studentname,maths_score,phy_score,chem_score from student_details where studentname='%s'"%name
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print("Student Name=",data[0])
# print("Maths Score=",data[1])
# print("Physics Score=",data[2])
# print("Chemistry Score=",data[3])