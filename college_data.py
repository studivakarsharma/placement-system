import college_management_class as Cls
import os
import sys

def clear_terminal():
    # 'nt' indicates Windows; otherwise, assume macOS/Linux ('posix')
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

P = Cls.PlacementManager()

Manual = """
--- Placement Management System ---
1. Add a New Student
2. Add a New Company
3. View All Students
4. View All Company
5. Find Eligible Students for a Company
6. Exit
Select an option:
"""
while True:
    
    try:
        Choice = int(input(Manual))
    except ValueError:
        print("\nInvalid input! Please enter a number between 1 and 6.")
        input("Press Enter to continue...")
        continue

    match Choice:
        
        case 1 :
            print("\n-----Adding a New Student------\n")
            S_Name = input("Enter Student Name: ").strip().lower()
            S_Roll = int(input("Enter Roll_no: "))
            S_CGPA = float(input("Enter CGPA: "))
            S_Skill = input("Enter Skill: ").strip().lower()
            S_Placement =True if input("Placement status (Y/N)").strip().lower() == 'y' else False
            S = Cls.Student(S_Name, S_Roll, S_CGPA, S_Skill, S_Placement)
            P.add_student(S)
            print("\n------Student successfully added-------\n")
            

        case 2:
            print("\n-----Adding a New Company-----\n")
            C_Name = input("Enter Company Name: ").strip().lower()
            C_Roll = input("Enter Roll of Job: ").strip().lower()
            C_CGPA = float(input("Enter Required CGPA: "))
            C_Skill = input("Enter Required Skills: ").strip().lower()
            C = Cls.Company(C_Name, C_Roll, C_CGPA, C_Skill)
            P.add_company(C)
            print("\n------Company successfully added-------\n")

        case 3:
            print("\n------Viewing Students-------\n")
            for i in range(len(P.Students)):
                print(f"{i+1}. {P.Students[i].Std_info()}")
            print("\n------Students successfully Viewed-------\n")

        case 4:
            print("\n------Viewing Students-------\n")
            for i in range(len(P.Companies)):
                print(f"{i+1}. {P.Companies[i].Criteria()}")
            print("\n------Companies successfully Viewed-------\n")
                            
        case 5:
            print("\n------Finding Eldgible Students-----\n")
            C_Name = input("Enter Company Name: ").strip().lower()
            qualified = P.find_eligible_students(C_Name)
            if qualified != None:
                for q in qualified:
                    print(q.Name)
            else:
                print("None")
            print("\n------Elidgible Students successfully Showed-------\n")

        case 6:
            print("\n---------Exiting From Program---------\n")
            clear_terminal()
            sys.exit()
        case _:
            print("Invalid input!")
            