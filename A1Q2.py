#Noh Daniel
#This code will make a report card based on the numbers given by the user

print("I will make your report card from last year, and all you have to do is")
print("answer a few questions! When asked for a grade, please type only the number. Here we go!")
name=input("What is your name?")
Sub1=input("What was your best subject in Grade 10?")
Sub1_gr=int(input("What was your grade?"))
Sub2=input("Second best subject?")
Sub2_gr=int(input("What was your grade?"))
Sub3=input("What was your worst subject?")
Sub3_gr=int(input("Grade?"))
Sub4=input("What was your second worst subject?")
Sub4_gr=int(input("And what was your final grade for that?"))
avr=(Sub1_gr+Sub2_gr+Sub3_gr+Sub4_gr)/4 #Formula for an average
print("Thank you! Now, I will write what I think your report card looked like last year.")

print("ST. MICHAEL'S COLLEGE SCHOOL")
print(name)
print("1515 Bathurst Street, Toronto, Ontario M5P 3H4")
print("416-653-3180 Fax 416-653-7704")
print("Mr. Pat Daly - Principal")
print("Fr. Andrew Leung, CSB – President")
print("REPORT CARD")
print("------------") #^^^This is copied of my report card last year^^^
print("Subject          Mark")
print(Sub1,"           ",Sub1_gr,"%")
print(Sub2,"           ",Sub2_gr,"%")
print(Sub3,"           ",Sub3_gr,"%")
print(Sub4,"           ",Sub4_gr,"%")
print("Average=", avr,"%")
if avr>=60 and avr<90:
#Any grade between this is a pass, but is not above a 90, which is the goal of most
#students I know.
    print("All in all,",name,"was a good student during their school year, ")
    print("and a pleasure to have at St. Michael's College School.")
    print("A little improvement is needed, but overall, ")
    print("he showed amazing growth in Goodness, Discipline, and Knowledge.")
elif avr<60:
#This is a fail, so the note will not praise them.
    print("All in all,",name,"needs improvement. At St. Michael's College School")
    print("our vision is to teach Goodness, Discipline, and Knowledge. We did not see")
    print("that from",name,", and we hope to see improvement next year.")
elif avr>90:
#This is the goal of most students, and what the school will reward you for.
    print("All in all,",name,"was a superb student during their school year, ")
    print("and a pleasure to have at St. Michael's College School.")
    print("He showed amazing growth in Goodness, Discipline, and Knowledge.")




