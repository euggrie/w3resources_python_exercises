                                ###############################
                                #                             #
                                #          Exercise 3         #
                                #     www.w3resource.com      #
                                ###############################


# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

##################################################################################################

import datetime

now = datetime.datetime.now()
print("Current time and date: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # .strftime: Return a string representing the date and time, controlled by an
                                          #  explicit format string