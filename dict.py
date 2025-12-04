students={}
def add():
    
    sid=int(input(" Enter Your ID : "))
    name=input(" Enter Your Name : ")
    age=int(input(" Enter Your Age : "))
    grade=int(input(" Enter Your Grade : "))
    
    students[sid]={
        "name" : name,
        "age" : age,
        "grade" : grade 
    }
    print("Student added successfully.")
    print(students)
    
    
    
def display_all():
    for sid in students:
        print(f"sid = {sid}, name = {students[sid]['name']}, age = {students[sid]['age']}, grade = {students[sid]['grade']}")


def search():
    sid=int(input(" Enter Students ID : "))
    if sid in students:
         print(f"sid = {sid}, name = {students[sid]['name']}, age = {students[sid]['age']}, grade = {students[sid]['grade']}")
         
    else:
        print(" Not Found !! ")

         
         
def update():
    sid = int(input(" Enter Student ID to update: "))
    if sid in students:
        grades = int(input(" Enter New Grade : "))
        students[sid]["grade"] = grades
        print("Grade updated successfully.")
        print(students)
    else:
        print("Student not found!")
    
    
while(True):
    print("--------Select Your Choice---------")
    print("1 . Add Students .")
    print("2 . Display All Students .")
    print("3 . Search A Student  .")
    print("4 . Update Grades  .")
    print("5 . Exit  .")

    a=int(input(" Enter Your Choice : "))
    if(a==1):
        add()
    elif(a==2):
        display_all()
    elif(a==3):
        search()
    elif(a==4):
        update()
    elif(a==5):
        print("Exiting...")
        break
    else:
        print("Enter Valid Choice !! ")
