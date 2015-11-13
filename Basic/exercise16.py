                                ###############################
                                #                             #
                                #          Exercise 16        #
                                #     www.w3resource.com      #
                                ###############################


# Write a Python program to get the difference between a given number and 17, if the number is greater
# than 17 return double the absolute difference
#################################################################################################

num = int(input("Enter a number: "))
a = 17

def calc(num):
    if num <= a:
        b = a - num
        print(b)
    elif num > a:
        c = 2 * abs(a-num)
        print(c)

calc(num)