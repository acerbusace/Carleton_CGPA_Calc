# AUTHOR: Alexkumar Patel
# Description:
#   Carleton CGPA calculator -> Calculates your Carleton CGPA
#   It does not take into account full credit courses
#   ^ work around is to enter full credit courses twice
# Python Version: 3.6.1

print('Welcome to Carleton CGPA calculator!')
print('Instructions: ')
print('\tEnter the "letter grade" for your courses')
print('\tEnter "calc" when want to calculate your CGPA')
print('Note: enter the letter grade for your full credit courses twice')

# letter grades and their correspodning CGPA values
gradesDef = {'D-': 1,
                 'D': 2,
                 'D+': 3,
                 'C-': 4,
                 'C': 5,
                 'C+': 6,
                 'B-': 7,
                 'B': 8,
                 'B+': 9,
                 'A-': 10,
                 'A': 11,
                 'A+': 12}

sum = 0
count = 0

# input loop from user
# get letter grades -> convert them to CGPA -> sum them up
# calc -> calculates the CGPA and exits
# note: invalid input (non letter grades), will result in invalid input prompt
while True:
    # get letter grade from user
    grade = input('Enter the letter grade for you course: ')
    grade = grade.upper()

    if grade == 'CALC':
        if count == 0:
            print('Your CGPA is 12!!!')
        else:
            print('Your CGPA is ' + str(sum / count))
        break
    elif grade in gradesDef:
        sum += gradesDef[grade] / 2
        print(grade + ' -> ' + str(gradesDef[grade]) + ' | ' + str(sum) + '  ' + str(count))
        count += 0.5
    else:
        print('Invalid input: please only enter letter grades (i.e a+, B-, etc...)')
