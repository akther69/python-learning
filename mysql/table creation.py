# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="Employeee_management")
# mycursor=db.cursor()
# sql="create table employee_details(id int auto_increment,name varchar(10),email varchar(50),phone bigint(10),primary key(id))"
# mycursor.execute(sql)
# db.commit()
# print("added table")


#work
#create a table inside student_management with fields
# studentname,school_name,department,maths_score,phy_score,chem_score


# import pymysql
# dbconnection=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=dbconnection.cursor()
# sql="create table student_details(id int auto_increment,studentname varchar(60),schoolname varchar(70),department varchar(88),maths_score int,phy_score int,chem_score int,primary key(id))"
# mycursor.execute(sql)
# dbconnection.commit()