import csv
from Labs.My_Modules import EmailCheckModule as e

def check_email(email):
    if '@@' in email:
        return False

    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@', 1)
            if username and domain:
                x, y = domain.split('.', 1)
                if x and y:
                    return True
        except ValueError:
            return False
    return False



file= open("people2.csv","r",newline="")
reader=csv.reader(file)


data=list(reader)

names=[]
emails=[]

for i in range(1,len(data)):
    names.append(data[i][0])
    emails.append(data[i][1])



valid_emails=list(filter(check_email,emails))

print('this is valid emails :')
print()
for i in valid_emails:
    print(i)

print('--------------------------------------------------------')

print('Number of valid emails is :',len(valid_emails))

print('--------------------------------------------------------')

e.number_of_domains(valid_emails)



