#HYBRID INHERITANCE
#it is the combination of single,multiple,hierarical,multilevel inheritance
# class university:
#     def __init__(self,university_name,location):
#         self.univer_name=university_name
#         self.location=location
#     def display_university(self):
#         print("University name:",self.univer_name)
#         print("Location",self.location)
# class college(university):
#     def __init__(self,college_name,college_email,university_name,location):
#         university.__init__(self,university_name,location)
#         self.college_name=college_name
#         self.college_email=college_email
#     def display_college(self):
#         print("College name:",self.college_name)
#         print("College Email:",self.college_email)
# class branch(university):
#     def __init__(self,branch_name,university_name,location):
#         university.__init__(self,university_name,location)
#         self.branch_name=branch_name
#     def display_branch(self):
#         print("Branch:",self.branch_name)
# class student(college,branch):
#     def __init__(self,student_name,rollno,college_name,college_email,university_name,location,branch_name):
#         college.__init__(self,college_name,college_email,university_name,location)
#         branch.__init__(self,branch_name,university_name,location)
#         self.student_name=student_name
#         self.rollno=rollno
#     def display_student(self):
#         print("Student name:",self.student_name)
#         print("roll no:",self.rollno)
#         print("College name: ",self.college_name)
#         print("College Email:",self.college_email)
#         print("University name:",self.univer_name)
#         print("Location:",self.location)
#         print("branch:",self.branch_name)
# obj=student("suhaib",20104167,"hindusthan","20104167@hicet.ac.in","anna university","coimbatore","CSE")
# obj.display_student()
