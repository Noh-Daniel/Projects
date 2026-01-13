total_word=""
count=int((input("How many words do you want to print?")))
for x in range (1, count+ 1):
    word=input('Word#'+ str(x)+':')
    total_word=total_word+word+('')
print(total_word)