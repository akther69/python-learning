import pymysql
db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
mycursor=db.cursor()
limit=int(input("Enter the limit="))
sql = "select * from student_details limit %d"%limit
mycursor.execute(sql)
data=mycursor.fetchall()
print(data)