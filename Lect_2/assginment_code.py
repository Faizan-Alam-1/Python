# Date : 1/10/23

'''
Assignment_coding - 2
Take input from user integer and ouput will be sum of two digit.
Example :
input --- 52  ,  12345 ---> 1+2+3+4+5
ouput -- 7 

'''



user = "Enter the number\n"
ans  = input(user)
char1 =  ans[0] # 1
char2 = ans[1] # 2
char3 = ans[2] # 3
char4 = ans[3]  # 4
char5 = ans[4] # 5

# typecaseting   
char1_int = int(char1)
char2_int = int(char2)
char3_int = int(char3)
char4_int = int(char4)
char5_int = int(char5)

sum = char1_int+char2_int+char3_int+char4_int+char5_int 

print(sum)






