                                ###############################
                                #                             #
                                #          Exercise 30        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program that will accept the base and height of a triangle and compute the area.

################################################################################################
base = int(input("Enter base of the triangle: "))
height = int(input("Enter height of the triangle "))

def area(b, h):
    return (h * b) / 2

print("The area of the triangle is : ")
print(area(base, height))
