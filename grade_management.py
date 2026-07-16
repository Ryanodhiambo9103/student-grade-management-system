students={}

def askCredentials():
 name=input("What is your name?")    
 admission_no=input("What is your admission number?")
 score=int(input("What did you score in the test>"))
 mobile_number=input("Please enter your parent's or gurdian's number")
 if score>=80:
    print("Exellent,keep it up!")
 elif score>=70: 
    print("Very Good!") 
 elif score>=60:
    print("Good!")
 elif score>=50:
    print("Fair!")
 elif score>=40:
    print("Put more effort!")
 else :
    print("Fail,you have the potential!") 

 students[admission_no]={
         "name":name,
         "score":score,
         "mobile_number":mobile_number
         }         

print("WELCOME TO THE GRADE MANAGEMENT SYSTEM")
who=input("Are you a teacher or student?")
if who=="teacher":
    Number=int(input("How many students are in your class?"))  

    for r in range(Number):
       askCredentials() 



    print(students)
elif who=="student":
  sub=input("Enter your admission number?")

  if sub in students:
     print(students[sub])
  else:
     print("Admission number not found please contact your teacher!")
       