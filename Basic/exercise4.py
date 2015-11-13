                                ###############################
                                #                             #
                                #          Exercise 4         #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program which accept the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504


##################################################################################################
import math
r = float(input("Enter radius of the circle : "))
def area(r):
    return math.pi * (r)*(r)

print("Area = " + str(area(1.1)))


