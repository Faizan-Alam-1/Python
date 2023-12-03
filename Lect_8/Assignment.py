# Print even number from 1 to 100, using loop and store ur even number in list and then print the even number.print.print.

def check_even(times):
  
    even_num_list = []
    for i in range(0 ,times):
     num = int(input("Enter number\n"))
     if num % 2 == 0:
        even_num_list.append(num)

    prints_even_num(even_num_list)    

  
def prints_even_num(even_num_list):
     for item in even_num_list:
        print(f'Even number {item}')    





times= int(input("Please enter times\n"))
check_even(times)




















   