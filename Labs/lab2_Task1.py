
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