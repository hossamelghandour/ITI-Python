from My_Modules import EmailCheckModule as e
    

def name_email():
    for i in range(5):
        name=input('Enter your name :').strip()
        if name=="" or name.isdigit():
            print('invalid name')
            continue

        email=input('Enter your Email: ')
        try:
            if e.check_email(email):
                print(f"your name is: {name}\nyour email is: {email}")
                break
            else:
                print('invalid email')
        except :
            raise ValueError('invalid email')
    else:
        print('You Are Blocked!!!')



name_email()