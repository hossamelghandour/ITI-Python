
def mariopyramids():
    for i in range(1,5):
        print(' '*(4-i) + '*'*i)


def mariopyramids_list(List):
    for i in range(5):
        List[4-i]="*"
        print(List)