from My_Modules import EmailCheckModule as e

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