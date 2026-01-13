count=int(input("How many words would you like to print? :"))
word=(" ")
if count<=0:
    print("Please pick a number above 0 :")
else:
    for x in range(count):
        word1=input("What word would you like to add? :")
        word=word + ' ' + word1
    print(word)
