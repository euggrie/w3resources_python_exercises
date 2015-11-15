                                ###############################
                                #                             #
                                #          Exercise 8         #
                                #     www.w3resource.com      #
                                ###############################


#  Write a Python function that takes a list of words and returns the length of the longest one.

####################################################################################################################

def find_longest_word(li):
    word = []
    for n in li:
        word.append((len(n), n))
    word.sort()
    print(word)
    return max(word)

print(find_longest_word(["PHP", "Exercises", "Backend"]))


