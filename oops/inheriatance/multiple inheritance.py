#multiple inheritance means a child class that can access two or more parent class
# class school:
#     def school_details(self,school_name,location):
#         self.schoolname=school_name
#         self.location=location
#     def school_display(self):
#         print("_____school details_____")
#         print("school name",self.schoolname)
#         print("location",self.location)
#         print()
# class parent:
#     def parent_details(self,parent_name,address):
#         self.parent_name=parent_name
#         self.address=address
#     def parent_display(self):
#         print("_____parent details_____")
#         print("parent name",self.parent_name)
#         print("address=",self.address)
#         print()
# class student(school,parent):#student class that inherit both and parent class
#     def student_details(self,stuname,rool,dept):
#         self.stuname=stuname
#         self.rollno=rool
#         self.dept=dept
#     def display_student(self):
#         print("_____student details_____")
#         print("school name", self.schoolname)
#         print("location", self.location)
#         print("parent name", self.parent_name)
#         print("address=", self.address)
#         print("student name",self.stuname)
#         print("roll no=",self.rollno)
#         print("department=",self.dept)
# obj=student()
# obj.school_details("holy cross","devarshola")
# obj.parent_details("shajahan","mayfiels")
# obj.student_details("suhaib",123,"CSE")
# obj.parent_display()
# obj.school_display()
# obj.display_student()


#task
class company:
    def company_details(self,company_name,location):
        self.companyname=company_name
        self.location=location
    def company_display(self):
        print("company details_____")
        print("company name",self.companyname)
        print("location",self.location)
        print()
# class team_leader:
#     def teamleader_details(self,teamleadername,department):
#         self.teamleader=teamleadername
#         self.department=department
#     def teamleader_display(self):
#         print("team leader details_____")
#         print("team leader name", self.teamleader)
#         print("department=", self.department)
#         print()
# class worker(company,team_leader):#student class that inherit both and parent class
#     def worker_details(self, empname, designation, salary):
#         self.empname=empname
#         self.designation=designation
#         self.salary=salary
#     def worker_student(self):
#         print("worker details_____")
#         print("company name", self.companyname)
#         print("location", self.location)
#         print("team leader name", self.teamleader)
#         print("department=", self.department)
#         print("empname",self.empname)
#         print("roll designation=",self.designation)
#         print("salary=",self.salary)
# obj=worker()
# obj.company_details("luminar","kakkanad")
# obj.teamleader_details("suhaib","cse")
# obj.worker_details("akther","promotor",1300)
# obj.worker_student()
# obj.teamleader_display()
# obj.company_display()


#with using constructor
# class company:
#     def __init__(self,company_name,location):
#         self.companyname=company_name
#         self.location=location
#     def company_display(self):
#         print("company details_____")
#         print("company name",self.companyname)
#         print("location",self.location)
#         print()
# class team_leader:
#     def __init__(self,teamleadername,department):
#         self.teamleader=teamleadername
#         self.department=department
#     def teamleader_display(self):
#         print("team leader details_____")
#         print("team leader name", self.teamleader)
#         print("department=", self.department)
#         print()
# class worker(company,team_leader):#student class that inherit both and parent class
#     def __init__(self,company_name,location,teamleadername,department,empname, designation, salary):
#         company.__init__(self,company_name,location)
#         team_leader.__init__(self,teamleadername,department)
#         self.empname=empname
#         self.designation=designation
#         self.salary=salary
#     def worker_student(self):
#         print("worker details_____")
#         print("company name", self.companyname)
#         print("location", self.location)
#         print("team leader name", self.teamleader)
#         print("department=", self.department)
#         print("empname",self.empname)
#         print("roll designation=",self.designation)
#         print("salary=",self.salary)
# obj=worker("luminar","kakkanad","suhaib","cse","akther","promotor",1300)
# obj.worker_student()
# obj.teamleader_display()
# obj.company_display()

#task
# class theatre:
#     def __init__(self,theater_name,place):
#         self.theatre_name=theater_name
#         self.place=place
#     def theatre_display(self):
#         print("theatre name",self.theatre_name)
#         print("place",self.place)
# class movie:
#     def __init__(self,title,director):
#         self.title=title
#         self.director=director
#     def movie_display(self):
#         print("title=",self.title)
#         print("director",self.director)
# class booking(theatre,movie):
#     def __init__(self,theater_name,place,title,director,num_of_user,time):
#         theatre.__init__(self,theater_name,place)
#         movie.__init__(self,title,director)
#         self.num_of_user=num_of_user
#         self.time=time
#     def booking_display(self):
#         print("theatre name", self.theatre_name)
#         print("place", self.place)
#         print("title=", self.title)
#         print("director", self.director)
#         print("number of user=",self.num_of_user)
#         print("time=",self.time)
# obj1=booking("mint","sulthan bathery","turbo","vyshak",5,"12:00 AM")
# obj2=booking("aiswarya","sulthan bathery","avesham","vyshak",5,"12:00 AM")
# obj1.booking_display()
# print()
# obj2.booking_display()