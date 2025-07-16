
from My_Modules import MultiplicationTableModule as mt
from My_Modules import MarioPyramidsModule as mario 
from My_Modules import EmailCheckModule as e

# Task 1 : Fill an array of 5 elements from the user, Sort it in descending and ascending orders 
# then display the output.

List=[]
for i in range(5):
    number=input('Enter Number'+'\n')
    if number.isdigit():
        List.append(int(number))
    else:
        print('Enter digit number')
        continue

print("old List is: ",List)

for i in range(len(List)):
    for j in range(0,len(List)-i-1):
        if List[j] > List[j+1]:
            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp

print('ascending List is: ',List)

for i in range(len(List)):
    for j in range(0,len(List)-i-1):
        if List[j] < List[j+1]:
            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp

print('descending List is: ',List)

################################################################

# Task 2 : Mario Pyramids

List = [" ", " ", " ", " ", " "]

mario.mariopyramids_list(List)

############################################################

# Task 3 : Write a program that generate a multiplication table from 1 to the number passed.

x = int(input('Enter Number: '))
table = mt.multitable_from1_listed(x)
print(table)

############################################################

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


