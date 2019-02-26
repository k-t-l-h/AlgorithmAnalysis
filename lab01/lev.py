from random import randint

def string_generator(n): 
    res = "" 

    for i in range(n):
        res += chr(randint(0, 25)+97)
    return res


def classic_levenshtein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    row1 = [x for x in range(l2 + 1)]  
    row2 = [1] 
    print(row1)

    for i in range(1, l1 + 1):  
        for j in range(1, len(row1)):  
            if s1[i - 1] != s2[j - 1]:  #если символы не совпадают
                row2.append(min(row1[j] + 1,  
                                row2[j - 1] + 1,
                                row1[j - 1] + 1))
            else:
                row2.append(min(row1[j] + 1,  
                                row2[j - 1] + 1,
                                row1[j - 1])) 

        print(row2)
        row1 = row2  
        row2 = [i + 1]

    return row1[-1]  #возвращает правый нижний элемент матрицы

for i in range(1, 8):
    one = input()
    two = input()
    print(one, two)
    print(classic_levenshtein(one, two))

