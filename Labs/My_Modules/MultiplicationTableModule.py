def multitable_from1(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(f"{i}x{j}={i*j}")
        print()



def multitable_from1_listed(x):
    result = []
    for i in range(1, x + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        result.append(row)
    return result