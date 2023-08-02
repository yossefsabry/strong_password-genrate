# ---------------------------------------
# -- making apassword genretor ----------
# ---------------------------------------

# start import models

import string
import random

# make list for password and empty list for the index when i do loop
# welcome massage 
print('-'*80)
print(" strong genrate password >> yossefsabry".center(80,'-'))
print('-'*80)

# start variables
printable_password = string.punctuation + string.ascii_letters + string.digits

loop_list = []

password_genrate = []

# making loop for append item in loop_list
for i in printable_password:

    loop_list.append(i)

# start def for input count that is the count for password 
def  genrate(count):
    
    '''
        def for count that the the count
        for number in the password
    '''

    # while loop for end the append when count eqeul to zero 
    while count > 0 :

        count_loop = random.randint(0,61)

        random_list = loop_list[count_loop]

        password_genrate.append(random_list)

        count -=1  # every time loop done the count dicrease one


# massage for the user if he want to change the count for def => the password number 

change_number = input("- do you want change the number for password (yes = y , no = n)? ").strip().capitalize()


# start if condition if the user want to change the nubmer for the password in the def => count

if change_number == "Yes" or change_number == "Y":

    genrate(count=int(input("- enter the number for password : ")))

    print("".join(password_genrate))


else:

    genrate(20)

    print("".join(password_genrate))


# making by yossef sabry @
# making by yossef sabry @
# making by yossef sabry @