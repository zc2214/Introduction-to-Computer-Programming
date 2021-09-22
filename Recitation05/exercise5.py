#def functions
def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#main program
score1 = int(input('Enter first score: '))
print('The letter grade is:',determine_grade(score1))
score2 = int(input('Enter second score: '))
print('The letter grade is:',determine_grade(score2))
score3 = int(input('Enter third score: '))
print('The letter grade is:',determine_grade(score3))
score4 = int(input('Enter fourth score: '))
print('The letter grade is:',determine_grade(score4))
score5 = int(input('Enter fifth score: '))
print('The letter grade is:',determine_grade(score5))

print()

average = calc_average(score1, score2, score3, score4, score5)
print('The average test score is:',average)
print('The letter grade is:',determine_grade(average))
