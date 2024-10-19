#for connecting the python and mysql we need a package known as: pymysql
#pip install pymysql
#setting:interpreter--->package---->pymysql---->install

# import pymysql
# dbconnection=pymysql.connect(host="localhost",user="root",password="")
# #what is cursor object in mysql
# #it is an object that is used to execute your sql command and also used to fetch datas from database
# mycursor=dbconnection.cursor()
# sql="create database Employeee_management"
# mycursor.execute(sql)
# print("New Database Created")

# import pymysql
# dbconnection=pymysql.connect(host="localhost",user="root",password="")
# mycursor=dbconnection.cursor()
# sql="create database student_management"
# mycursor.execute(sql)
# print("database created")