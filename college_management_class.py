class Student:
    def __init__(self, Name, Roll_No, CGPA, Core_Skill, Placement_Status):
        params = locals()
        for key, value in params.items():
            if key != "self":
                setattr(self, key, value)

    def Update_CGPA(self,new_CGPA):
        self.CGPA = new_CGPA

    def Std_info(self):
        return {"Name" : self.Name, "Roll_no" : self.Roll_No, "Skill" : self.Core_Skill, "CGPA" : self.CGPA, "Placement_Status" : self.Placement_Status }
    
class Company:
    def __init__(self, Name, Req_Role, Req_CGPA, Req_Skill):
        params =locals()
        for key, value in params.items():
            if key!="self":
                setattr(self, key, value)

    def Criteria(self):
        return {"Name" : self.Name, "Role" : self.Req_Role, "CGPA" : self.Req_CGPA, "Skill" : self.Req_Skill}
        
class PlacementManager:
    
    def __init__(self):
        self.Students = []
        self.Companies = []

    def add_student(self,other):
        self.Students.append(other)
    def add_company(self, other):
        self.Companies.append(other)
    def __eq__(self,key):
        return self.Name == key
    def find_eligible_students(self, C_Name):
        target = C_Name.strip().lower()
        Criteria = None
        for company in self.Companies:
            if company.Name == target:
                Criteria = company.Criteria()
                break
        if Criteria is None:
            print("Company not Found!")
            return []
        Qualified = [
            student
            for student in self.Students
            if student.CGPA >= Criteria["CGPA"]
            and student.Core_Skill == Criteria["Skill"]
        ]

        if not Qualified:
            print("None Qualified!")
            return []
        
        return Qualified

if __name__ == "__main__":
    s1 = Student("Divakar", 102, 9.5, "Software", False)
    c1 = Company("infa", "Devloper ", 7.7, "Software")

    p1 = PlacementManager()

    p1.add_student(s1)
    p1.add_company(c1)
    quailfied = p1.find_eligible_students("infa")
    for q in quailfied:
        print(q.Name)