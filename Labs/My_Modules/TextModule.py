def count_vowels(word):
    vowels='aeiouAEIOU'
    count=0
    for i in word:
        if i in vowels:
            count+=1
    print(count)



def location_of_i(word):
    for i in range(len(word)):
        if word[i] == 'i':
            print(f'i in index No. {i}')