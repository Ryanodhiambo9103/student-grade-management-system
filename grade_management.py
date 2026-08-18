students={}

def askCredentials():
 name=input("What is your name?")    
 admission_no=input("What is your admission number?")
 score=int(input("What did you score in the test>"))
 mobile_number=input("Please enter your parent's or gurdian's number")
 def grade_score():
  if score>=80:
    return("A")
  elif score>=70: 
    return("B") 
  elif score>=60:
    return("C")
  elif score>=50:
    return("C-")
  elif score>=40:
    return("D")
  else :
    return("E") 
  

 comment = {
             "A": "Excellent,work!",
             "B": "Very good!",
             "C": "Nice!",
             "C-": "Good!",
             "D": "Almost there!",
             "E": "Need to put more effort"
                         }
    
    

 students[admission_no]={
         "name":name,
         "score":score,
         "mobile_number":mobile_number,
         "grade":grade_score(),
         "remarks":comment[grade_score()]     
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
       