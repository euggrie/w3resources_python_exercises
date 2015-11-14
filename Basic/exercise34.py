                                ###############################
                                #                             #
                                #          Exercise 34        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to sum of two given integers. However if the sum is between 15 to 20 it will return 20.

###############################################################################################################

def prog(x,y):
    s = x + y
    if s in range(15, 21, 1):
        s = 20

    return s

print(prog(3,25))