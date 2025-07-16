from My_Modules import MultiplicationTableModule as mt


# Task 3 : Write a program that generate a multiplication table from 1 to the number passed.

x = int(input('Enter Number: '))
table = mt.multitable_from1_listed(x)
print(table)