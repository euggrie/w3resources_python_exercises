                                ###############################
                                #                             #
                                #          Exercise 12        #
                                #     www.w3resource.com      #
                                ###############################



#  Write a Python program to count the occurrences of each word in a given sentence.

######################################################################################

def prog(string):
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print(prog("the quick brown fox jumps over the lazy dog."))


