                                ###############################
                                #                             #
                                #          Exercise 9         #
                                #     www.w3resource.com      #
                                ###############################



#  Write a Python program to remove the nth index character from a non empty string.

########################################################################################

def prog(string, n):
    first = string[:n]
    last = string[n+1:]
    return first + last

print(prog("Python", 3))