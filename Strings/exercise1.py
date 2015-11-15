                                ###############################
                                #                             #
                                #          Exercise 1         #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to calculate the length of a string.

##########################################################################################################

string = input("Enter some text: ")

def prog(txt):
    count = 0
    for char in txt:
        count += 1
    return count

print(prog(string))