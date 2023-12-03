 # input()
# range()
# len ()
# print()

# how can make my own function

 # own 

# def sum(num1, num2):
#     add = num1+num2
#     return add


# sum()

# def say():
#     print("Hello world")

# say()


# module , pakage


from tkinter import *

root = Tk()

root.title("Ram's application")
root.geometry("550x550")
root.resizable(False,False)

txt =  Label(root , text = "hello world")
txt.pack()

def doing():
    print("hello , i'm btn")


btn = Button(root , text="i'm button" , command=doing)
btn.pack()



root.mainloop()