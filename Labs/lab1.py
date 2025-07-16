from My_Modules import MultiplicationTableModule as mt
from My_Modules import MarioPyramidsModule as mario
from My_Modules import TextModule as text


# Task1 : Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.

word=input('enter word : ')
text.count_vowels(word)


###############################################

# Task2 :  Write a program that prints the locations of "i" character in any string you added.

word=input('enter word : ')
text.location_of_i(word)


################################################

# Task3 : Write a program that generate a multiplication table from 1 to the number passed
x = input('Enter Number')
x=int(x)
mt.multitable_from1(x)

################################################

# Task4 : Write a program that build a Mario pyramid like below
mario.mariopyramids()