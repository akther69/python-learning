#min and max in Mysql
# sql=select min(maths_score) from table_name
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql = "select min(maths_score) from student_details"
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print(data)


#max
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql = "select max(maths_score) from student_details"
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print(data)


#max of two or more
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql = "select max(maths_score),max(phy_score),max(chem_score) from student_details"
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print(data)


#average
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql = "select avg(maths_score),avg(phy_score),avg(chem_score) from student_details"
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print(data)


#write an sql query the fetch details of student that scored max mark in maths?
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql = "select * from student_details where maths_score=(select max(maths_score) from student_details)"
# mycursor.execute(sql)
# data=mycursor.fetchone()
# print(data)