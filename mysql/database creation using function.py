# create a database product
# create 2 tables
# product details customer details
# id,pro_name,price,product code
# id,customer name,product code,delivery addrress


#database creation
# def database_creation(dbname):
#     import pymysql
#     db = pymysql.connect(host="localhost", user="root", password="")
#     mycursor=db.cursor()
#     sql=f"create database {dbname}"
#     mycursor.execute(sql)
#     db.commit()
#     print(f"{dbname} database created successfully")
# database_creation("product_management")


#database table creation
# def table_creation(dbname,tbname,*coloumn):
#     import pymysql
#     db=pymysql.connect(host="localhost",user="root",password="",database=dbname)
#     mycursor=db.cursor()
#     colum_value=','.join(coloumn)
#     sql=f"create table {tbname}({colum_value})"
#     mycursor.execute(sql)
#     db.commit()
#     print("Table created successfully")
# table_creation("product_management","product_details",'id int auto_increment','product_name varchar(100)','product_code varchar(100)','primary key(id)')
# table_creation("product_management","customer_details",'id int auto_increment','customer_name varchar(100)',"product_code varchar(100)","delivery_address varchar(100)","primary key(id)")


# table insertion
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="product_management")
# mycursor=db.cursor()
# product_name=input("Enter the product name=")
# price=int(input("Enter the price="))
# product_code=input("Enter the product code=")
# sql="insert into product_details(product_name,price,product_code) value('%s',%d,'%s')"%(product_name,price,product_code)
# mycursor.execute(sql)
# db.commit()
# print("insertion successfull")


#table insertion
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="product_management")
# mycursor=db.cursor()
# customer_name=input("Enter the customer name=")
# product_code=input("Enter the product code=")
# delivery_address=input("Enter the customer address=")
# sql="insert into customer_details(customer_name,product_code,delivery_address) value('%s','%s','%s')"%(customer_name,product_code,delivery_address)
# mycursor.execute(sql)
# db.commit()
# print("insertion successfull")


#joining
# import pymysql
# db=pymysql.connect(host="localhost",user="root",password="",database="product_management")
# mycursor=db.cursor()
# sql="select product_details.product_name,product_details.product_code,product_details.price,customer_details.customer_name,customer_details.product_code,customer_details.delivery_address from product_details inner join customer_details on product_details.product_code=customer_details.product_code"
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     print("Name=", i[3])
#     print("Product Name=", i[0])
#     print("Product Code=", i[1])
#     print("Price=", i[2])
#     print("Delivery Address=", i[5])
#     print()


#data insertion using function
# def insertion(dbname,tbname,**kwargs):
#     import pymysql
#     db=pymysql.connect(host="localhost", user="root", password="", database=dbname)
#     mycursor = db.cursor()
#     keys=",".join(kwargs.keys())
#     values=",".join(f"'{i}'"if not str(i).isdigit() else str(i) for i in kwargs.values())
#     sql=f"insert into {tbname} ({keys}) values({values})"
#     mycursor.execute(sql)
#     db.commit()
#     print("insertion successfull")
# # insertion("employeee_management","employee_details",name="paapa",email="paapa@gmail.com",phone=76545654766)
# insertion("product_management","product_details",product_name="cushion",price=269,product_code="159Z")


#delete using function
#create a function that takes 3 arguments,databasename,table_name,id
# def deletion(dbname,tbname,id):
#     import pymysql
#     db=pymysql.connect(host="localhost",user="root",password="",database=dbname)
#     mycursor=db.cursor()
#     data=f"select id from {tbname}"
#     mycursor.execute(data)
#     fetch=mycursor.fetchall()
#     for i in fetch:
#         if(id==i[0]):
#             sql=f"delete from {tbname} where id={id}"
#             mycursor.execute(sql)
#             db.commit()
#             print("deletion successfull")
#             break
#     else:
#         print("Enter the valid id")
# deletion("product_management","product_details",10)


#update using function
# def updation(dbname,tbname,id,**kwargs):
#     import pymysql
#     db=pymysql.connect(host="localhost",user="root",password="",database=dbname)
#     mycursor=db.cursor()
#     data=f"select id from {tbname}"
#     mycursor.execute(data)
#     fetch=mycursor.fetchall()
#     for i in fetch:
#         if(id==i[0]):
#             set_value=",".join(f"{keys}='{values}'" if not str(values).isdigit() else f"{keys}={values}" for keys,values in kwargs.items())
#             sql=f"update {tbname} set {set_value} where id={id}"
#             mycursor.execute(sql)
#             db.commit()
#             print("updation successfull")
#             break
#     else:
#         print("Enter the valid id")
# updation("product_management","product_details",5,product_name="dohar",price=999,product_code="1111A")