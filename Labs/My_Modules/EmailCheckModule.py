def check_email(email):
    if '@' in email and '.' in email:
        try:
            username,domain=email.split('@',1)
            if username and domain:
                x,y=domain.split('.',1)
                if x and y:
                    return True
        except ValueError:
            return False
    else:
        return False
    


def number_of_domains(emails):
    result = list(map(lambda x:x.split('@')[1],emails))
    result=set(result)
    counter = len(result)   
    print('this is distinct domains',result)
    print(f"Numbers of domain is :{counter}")



def check_authorization(name_password):
    name=input('Enter your name: ')
    
    for i in name_password:
        if i['name']==name:
            password=input('Enter your password: ')
            if i['password']==password:
                print('authorized')
            else :
                print('unauthorized')
            break
        else:
            print('invalid name')


def valid_emails(emails):
    return  filter(check_email,emails)