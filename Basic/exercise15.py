                                ###############################
                                #                             #
                                #          Exercise 15        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to get the volume of a sphere with radius 6

###################################################################################################
import math

r = 6

def calc(r):
    vol = (4/3) * math.pi * math.pow(r,3)
    print(vol)

calc(r)