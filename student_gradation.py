# 1. Jack's dictionary 
jack = { "name":"Jack Frost", 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20], 
         "assignment" : [80, 50, 40, 20] 
       } 
         
# 2. James's dictionary 
james = { "name":"James Potter", 
          "test" : [80, 80], 
          "lab" : [67.90, 78.72],
          "assignment" : [82, 56, 44, 30]
        } 
  
# 3. Dylan's dictionary 
dylan = { "name" : "Dylan Rhodes", 
          "test" : [78, 77], 
          "lab" : [80, 80],
          "assignment" : [77, 82, 23, 39]
        } 
          
# 4. Jessica's dictionary 
jess = { "name" : "Jessica Stone", 
         "test" : [40, 50], 
         "lab" : [69, 44.56], 
         "assignment" : [67, 55, 77, 21]
       } 
         
# 5. Tom's dictionary 
tom = { "name" : "Tom Hanks", 
        "test" : [65, 56], 
        "lab" : [50, 40.6], 
        "assignment" : [29, 89, 60, 56]
      } 

def calculate_average(marks):
    return float(sum(marks))/len(marks)

def calculate_average_marks(student):
    test_avg = calculate_average(student["test"])
    lab_avg = calculate_average(student["lab"])
    assignment_avg = calculate_average(student["assignment"])
    avg_marks = test_avg * 0.7 + lab_avg * 0.2 + assignment_avg * 0.1
    return avg_marks

def assign_grade(score):
    if score >= 90: grade = "O"
    elif score >= 80: grade = "A"
    elif score >= 70: grade = "B"
    elif score >= 60: grade = "C"
    elif score >= 50: grade = "D"
    else: grade = "E"
    return grade

students = [jack,james,dylan,jess,tom]
for student in students:
    name = student["name"]
    avg_marks = calculate_average_marks(student)
    grade = assign_grade(avg_marks)
    print("Student name: {0:18s}Average Marks: {1:2.2f}\tGrade: {2:4s}".format(name,avg_marks,grade))
