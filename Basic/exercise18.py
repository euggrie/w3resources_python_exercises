                                ###############################
                                #                             #
                                #          Exercise 18        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum

#######################################################################################################################

def calc(a,b,c):
    if a != b:
        z =  (a + b + c)
        print(z)
    elif a == b and b == c:
        y = 3 * (a + b + c)
        print(y)

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

calc(a,b,c)