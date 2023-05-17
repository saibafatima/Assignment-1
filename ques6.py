# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

my_list = [5, 12, 8, 27, 15, 9, 18, 4, 21, 30, 14, 3, 6, 19, 22, 33, 11, 25, 16, 7, 10, 20, 24, 13, 36]

for element in my_list :
    if element % 3 == 0:
        print(f"{element} is divisible by 3")
    else:
        print(f"{element} is not divivsible bt 3")