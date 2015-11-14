                                ###############################
                                #                             #
                                #          Exercise 24        #
                                #     www.w3resource.com      #
                                ###############################

# Write a Python program to test whether a passed letter is a vowel or not

#########################################################################################
vowels = ['a', 'e', 'i', 'o', 'u']
def prog(x):
    if x in vowels:
        return True
    else:
        return False
print("This letter is a vowel: ")
print(prog('z'))

