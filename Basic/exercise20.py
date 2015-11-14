                                ###############################
                                #                             #
                                #          Exercise 20        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def prog(string, n):
    result = ""
    for i in range(n):
        result = result + string
    return result

print(prog("abc",2))
print(prog("text",3))
