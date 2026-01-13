#Noh Daniel
#2023/10/18
#This program will ask a user how they are feeling that day, and write them a message
#corresponding with that feeling. If it is not the same feeling as written, it will
#say the feeling is invalid


feel=input("How are you feeling today? Great, Good, Okay, or Terrible?")
#Only these feelings.
if feel == "Great":
    print("That's amazing! I am glad you feel great!")
elif feel == "Good":
    print("That is good. I hope you can feel great soon!")
elif feel == "Okay":
    print("Ok. I hope your day improves!")
elif feel == "Terrible":
    print("I am so sorry to hear that! I hope you have a better day tomorrow.")
else:
    print("Invalid feeling. Please input one of the choices given.")
    #If not one of the feelings provided.

print("Thank you for participating. Have a great day tomorrow!")
