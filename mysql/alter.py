#alter
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql="alter table student_details add total int(5)"
# mycursor.execute(sql)
# db.commit()
# print("altered successfully")


# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# name=input("Enter the name of the student=")
# new_maths_score=int(input("Enter the new maths mark="))
# new_phy_score=int(input("Enter the new physics mark="))
# new_chem_score=int(input("Enter the new chemistry mark="))
# total=new_chem_score+new_phy_score+new_maths_score
# sql="update student_details set maths_score=%d,phy_score=%d,chem_score=%d,total=%d where studentname='%s'"%(new_maths_score,new_phy_score,new_chem_score,total,name)
# mycursor.execute(sql)
# db.commit()
# print("Updated successfully")


#more than one table adding
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql="alter table student_details add (phone bigint(10),email varchar(100))"
# mycursor.execute(sql)
# db.commit()
# print("altered successfully")


#add tablename after any table
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="product_management")
# mycursor=db.cursor()
# sql="alter table product_details add price varchar(100) after product_name"
# mycursor.execute(sql)
# db.commit()
# print("altered successfully")


#drop
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# sql="alter table student_details drop column phone,drop column parentname"
# mycursor.execute(sql)
# db.commit()
# print("droped successfully")

#alter table name
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="product_management")
# mycursor=db.cursor()
# sql="alter table product_details change column price price int(100)"
# mycursor.execute(sql)
# db.commit()
# print("changed successfully")

