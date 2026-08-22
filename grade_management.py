students={}

def askCredentials():
 name=input("What is the student's name?")    
 admission_no=input("What is the student's admission number?")
 score=int(input("What did the student score in the test>"))

 while score > 0 and score <= 100 :
  score = int(input("Please re-enter the student's score: "))
  
 mobile_number=input("Please enter the student's parent's or gurdian's number")
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
  
 grade = grade_score()

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
         "grade":grade,
         "remarks":comment[grade]     
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
       