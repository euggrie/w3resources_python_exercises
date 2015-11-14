                                ###############################
                                #                             #
                                #          Exercise 33        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

##########################################################################################################
def prog(a,b,c):
    if a == b or b == c or a == c:
        return 0
    else:
        return int(a + b + c)

print(prog(2,2,7))