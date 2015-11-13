                                ###############################
                                #                             #
                                #          Exercise 14        #
                                #     www.w3resource.com      #
                                ###############################

#Write a Python program to calculate number of days between two dates.

#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

##############################################################################################
from datetime import date
f_date = date(2014, 7, 2)
i_date = date(2014, 7, 11)
delta = i_date - f_date
print(delta.days)