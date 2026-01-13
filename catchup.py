student_name = input("Enter your name: ")
subject1 = input("Enter the name of subject 1: ")
subject2 = input("Enter the name of subject 2: ")
subject3 = input("Enter the name of subject 3: ")
subject4 = input("Enter the name of subject 4: ")

# Get user input for marks in each subject
mark1 = float(input(f"Enter your final mark in {subject1}: "))
mark2 = float(input(f"Enter your final mark in {subject2}: "))
mark3 = float(input(f"Enter your final mark in {subject3}: "))
mark4 = float(input(f"Enter your final mark in {subject4}: "))

# Calculate the average mark
average_mark = (mark1 + mark2 + mark3 + mark4) / 4

# Print the report card
print("\n========================")
print("      REPORT CARD")
print("========================")
print(f"Name: {student_name}")
print("\nSubject        Mark")
print("------------------------")
print(f"{subject1:<15}{mark1:.2f}")
print(f"{subject2:<15}{mark2:.2f}")
print(f"{subject3:<15}{mark3:.2f}")
print(f"{subject4:<15}{mark4:.2f}")
print("------------------------")
print(f"Average        {average_mark:.2f}")
print("========================")

# Generate a teacher comment based on the average mark
if average_mark >= 90:
    comment = "Excellent work! Keep it up!"
elif average_mark >= 80:
    comment = "Great job! Your hard work is paying off."
elif average_mark >= 70:
    comment = "Good work, but there's always room for improvement."
else:
    comment = "We should discuss ways to improve your grades."

print("\nTeacher Comment:")
print(comment)