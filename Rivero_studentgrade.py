name = input("Please enter your name: ")
section = input("Please enter your section: ")

prelim_grade = float(input("Please enter your Prelim grade: "))
if(prelim_grade < 40 or prelim_grade > 100):
    print("Invalid input of Prelim grade")
    exit()
midterm_grade = float(input("Please enter your Midterm grade: "))
if(prelim_grade < 40 or prelim_grade > 100):
    print("Invalid input of Midterm grade")
    exit()
finals_grade = float(input("Please enter your Finals grade: "))
if(prelim_grade < 40 or prelim_grade > 100):
    print("Invalid input of Finals grade")
    exit()

final = (prelim_grade * .3333) + (midterm_grade * .3333) + (finals_grade * .3333)
print(f"Your final grade is {final:.0f}")


if(final >= 99 and final <= 100):
    print("Your GPA is 1.00")
elif(final >= 96 and final <= 98):
    print("Your GPA is 1.25")
elif(final >= 93 and final <= 95):
    print("Your GPA is 1.50")
elif(final >= 90  and final <= 92):
    print("Your GPA is 1.75")
elif(final >= 87 and final <= 89):
    print("Your GPA is 2.00")
elif(final >= 84 and final <= 86):
    print("Your GPA is 2.25")
elif(final >= 81 and final <= 83):
    print("Your GPA is 2.50")
elif(final >=  78 and final <= 80):
    print("Your GPA is 2.75")
elif(final >= 75 and final <= 77):
    print("Your GPA is 3.00")
elif(final < 75):
    print("Your GPA is 5.00")
else:
    print("Invalid input of Grade")