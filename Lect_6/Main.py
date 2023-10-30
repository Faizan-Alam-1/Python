print("Thank you for chosing python pizza Deliveries\n")
bill = 0
Question = "Enter size of Pizza L , M  ,S\n"
size = input(Question)                   # small pizza $15 , Medium pizza $ 20 , Large Pizza $25 
add_pepperoni = input("Do you want peopperoni ? Y : N :  ")      # +$3
extra_cheese =  input("Do you want extra cheese? Y : N : ")      # $1

"lowercase -- a , b ,c, d   ----  uppercase ---- A , B, C "  

if size.upper() == 'L':
    bill = bill+25

    if add_pepperoni.upper() == 'Y':
         bill = bill+3
    if extra_cheese.upper() =='Y':
        bill  = bill+1
   

if size.upper() == 'M':
    bill = bill+20

    if add_pepperoni.upper() == 'Y':
         bill = bill+3
    if extra_cheese.upper() =='Y':
        bill  = bill+1


if size.upper() == 'S':
    bill = bill+15

    if add_pepperoni.upper() == 'Y':
         bill = bill+3
    if extra_cheese.upper() =='Y':
        bill  = bill+1


print(f"{bill}$"  )


 