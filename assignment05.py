print("Welcome to your Letter Grade Calculator\n")
#ask the user to enter their cooresponding grade based on the variable name. Remember to wrap the input around a float() so that we can use decimals. Ex.) float(input("What's your grade in ...: "))

math = float(input("What's your grade in Math: "))
science = float(input("What's your grade in Science: "))
english = float(input("What's your grade in English: "))
history = float(input("What's your grade in History: "))
worldLanguage = float(input("What's your grade in World Languages: "))
physicalEducation = float(input("What's your grade in Physical Education: "))

#store the average of all of the grades into the gpa variable (average is the sum of all 6 number grades divided by 6)
averageGrade = (math + science + english + history + worldLanguage +physicalEducation) / 6

#print the user's letter grade average based on their averageGrade. Remember, if the averageGrade is greater than or equal to 90, the letter grade is an A. If the averageGrade is greater than or equal to 80, the letter grade is a B. If the averageGrade is greater than or equal to 70, the letter grade is a C. If the averageGrade is greater than or equal to 60, the letter grade is a D. If the averageGrade is less than 60, the letter grade is an F. (HINT: I recommend using 5 condition statements in total, including 1 if statement, 3 elif statements, and an else statement)
if averageGrade >= 90:
    print("A")
elif averageGrade >= 80:
    print("B")
elif averageGrade >= 70:
    print("C")
elif averageGrade >= 60:
    print("D")
else:
    print("F")


#BONUS: add the appropriate if and else statements that tell the user if they can play sports
if averageGrade >= 70:
    print("You are eligible to participate in sports.")
else:
    print("You are not eligible to participate in sports.")
