#Noh
#This is an invoice maker. It will get the information of people's orders from a
#flying disk shop, and make an invoice based on it.

print("Welcome to Fred's Flying Disks! Please enter your information below to get an"
      "estimate on your order.")

name=input("What is your name?")
adr=input("What is your adress?")
disc=float(input("How many regular discs are you buying?"))
cus_disc=float(input("How many custom disc are you buying?"))
disc_pr=disc*8
cus_disc_pr=cus_disc*15
subtl=disc_pr+cus_disc_pr
tax=subtl*0.13
total= (tax+subtl)-(subtl*0.15)
discount=subtl*0.15
rounded_number=format(total,".3f")
print("                                INVOICE")
print("==================================================================================")
print("Busy Frisbee")
print("9183 Sesame Street, M6A 7E1")

print("Bill to:")
print(name)
print(adr)
print("Description             Quantity      Unit price               Amount")
print("Standard Disc          ",disc,"        $8.00                   $",disc_pr,"0")
print("Custom Disc            ",cus_disc,"    $15.00                  $",cus_disc_pr,"0")
print("                                                    Subtotal:   $",subtl,"0")
print("                                                    Tax(13% HST)$",tax)
print("                                                    Discount    $",discount)
print("                                                    Total       $",total)