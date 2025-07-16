
from My_Modules import EmailCheckModule as e

# Task 4 : Ask the user for his name then confirm that he has entered his name(not an empty string/integers). 
# then proceed to ask him for his email and print all this data(Bonus) check if it is a valid email or not

while True:
    name=input('Enter your name :').strip()
    if name=="":
        print('invalid name')
    elif name.isdigit():
        print('invalid name')
    else:
        break

email=input('Enter your email :')
e.check_email(email)


print(f"Your Name is: {name} and Your Email is: {email}")