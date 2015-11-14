                                ###############################
                                #                             #
                                #          Exercise 21        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an
#  appropriate message to the user.

##############################################################################################

n = int(input("Enter a number: "))
def prog(num):
    if num % 2 == 0:
        print("The number is even")
    elif num % 2 != 0:
        print("the number is odd")

prog(n)