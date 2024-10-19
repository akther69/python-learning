# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# name=input("Enter the name of the student=")
# data="select studentname from student_details"
# mycursor.execute(data)
# fetch=mycursor.fetchall()
# for i in fetch:
#     if(name==i[0]):
#         new_maths_score = int(input("Enter the new maths mark="))
#         new_phy_score = int(input("Enter the new physics mark="))
#         new_chem_score = int(input("Enter the new chemistry mark="))
#         sql="update student_details set maths_score=%d,phy_score=%d,chem_score=%d where studentname='%s'"%(new_maths_score,new_phy_score,new_chem_score,name)
#         mycursor.execute(sql)
#         db.commit()
#         break
# else:
#     print("Person not found")


#update name of student using department and id
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# dept=input("Enter the department=")
# id=int(input("Enter the id="))
# data="select id,department from student_details"
# mycursor.execute(data)
# fetch=mycursor.fetchall()
# for i in fetch:
#     if(dept==i[1] and id==i[0]):
#         newname=input("Enter the new name of the student=")
#         sql="update student_details set studentname='%s' where id=%d and department='%s'"%(newname,id,dept)
#         mycursor.execute(sql)
#         db.commit()
#         print("Updated successfully")
#         break
# else:
#     print("Enter the correct id and department")