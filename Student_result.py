print('''
========================================
      STUDENT GRADING SYSTEM
========================================
      Enter marks out of 100

Subjects:
1. English
2. Mathematics
3. Science
4. Social Science
5. Computer

----------------------------------------
Please enter the marks carefully.
========================================''')
eng_marks = int(input('Marks of English: '))
maths_marks= int(input('Marks of Mathematics: '))
science_marks = int(input('Marks of Science: '))
sst_marks = int(input('Marks of Social Science: '))
computer_marks = int(input('Marks of computer: '))

total_marks = eng_marks + maths_marks + science_marks + sst_marks + computer_marks
if eng_marks > 100 or maths_marks > 100 or science_marks > 100 or sst_marks > 100 or computer_marks > 100:
    print('--> Give marks out of 100!')
else:
    percentage = (total_marks/500)*100
    if percentage >= 90:
        Grade = 'A'
    elif percentage >= 75 :
        Grade = 'B'
    elif  percentage >= 60:
        Grade = 'C'
    elif percentage >= 33:
        Grade = 'D'
    else :
        Grade = 'Fail'
    if percentage >= 33 :
        Result = 'Pass'
    else :
        Result = 'Fail'
      
    print("""
========================================
         RESULT DECLARED
========================================
""")

    print("Total Marks     :", total_marks, "/500")
    print("Percentage      :", percentage, "%")
    print("Grade           :", Grade)
    print("Result          :", Result)

    print("""
========================================
   Thank you for using the program!
========================================
""")

        
