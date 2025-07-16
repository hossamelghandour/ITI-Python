
from My_Modules import EmailCheckModule as e


# Task 1 : Ask the user for his name then confirm that he has entered his name(not an empty string/integers). 
# then proceed to ask him for his email and print all this data(Bonus) check if it is a valid email or not


def name_email():
    for i in range(5):
        name=input('Enter your name :').strip()
        if name=="" or name.isdigit():
            print('invalid name')
            continue
        email=input('Enter your Email: ')
        
        if e.check_email(email):
            print(f"your name is: {name}\n your email is: {email}")
            break


name_email()


#######################################################################

# Task 2 : Numbers of domains

emails = ["ali@gmail.com","sara@yahoo.com","mohamed@outlook.com","noha@iti.gov.eg"]
e.number_of_domains(emails)


#######################################################################

# Task 3 : authorization of name and password

name_password = [{'name': 'hossam', 'password':'123'},{'name': 'hamdy', 'password':'456'},{'name': 'hassan', 'password':'789'}]
e.check_authorization(name_password)


###################################################################

# Task 4 : return only the valid email addresses

emails = [
    "ali@gmail.com",
    "sara@yahoo",
    "mohamed@outlook.com",
    "noha@iti.gov.eg",
    "invalidemail.com",
]

validemails = e.valid_emails(emails)
print(list(validemails))