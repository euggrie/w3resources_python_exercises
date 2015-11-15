                                ###############################
                                #                             #
                                #          Exercise 4         #
                                #     www.w3resource.com      #
                                ###############################


# Write a Python program to get a string from a given string where all occurrences of its first char have been changed
#  to '$', except the first char itself.
#  Sample String : 'restart'
#  Expected Result : 'resta$t'

####################################################################################################################

def prog(txt):
    char = txt[0]
    lenght = len(txt)
    txt = txt.replace(char, '$')
    txt = char + txt[1:]

    return txt

print(prog('restart'))


