L=int(input("Pick a length"))
W=int(input("Pick a width"))
if (L<0 or W<0):
    print("Please input a positive number!")
print(L,"*",W)
print(L*W)
print((L,"*",2),"+",(W,"*",2))
print((L*2),"+",(W*2))
print((L*2)+(W*2))
