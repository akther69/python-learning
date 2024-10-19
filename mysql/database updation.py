# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="employeee_management")
# mycursor=db.cursor()
# id=int(input("Enter the id="))
# newname=input("Enter the new name=")
# sql="update employee_details set name='%s' where id=%d"%(newname,id)
# mycursor.execute(sql)
# db.commit()
# print("Updated successfully")


#update student table maths score,physics score and chemistry score using student name
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="student_management")
# mycursor=db.cursor()
# name=input("Enter the name of the student=")
# new_maths_score=int(input("Enter the new maths mark="))
# new_phy_score=int(input("Enter the new physics mark="))
# new_chem_score=int(input("Enter the new chemistry mark="))
# sql="update student_details set maths_score=%d,phy_score=%d,chem_score=%d where studentname='%s'"%(new_maths_score,new_phy_score,new_chem_score,name)
# mycursor.execute(sql)
# db.commit()
# print("Updated successfully")