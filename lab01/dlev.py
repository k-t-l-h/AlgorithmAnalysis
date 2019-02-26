from random import randint

def string_generator(n): 
    res = "" 

    for i in range(n):
        res += chr(randint(0, 25)+97)
    return res

def damerau_levenshtein(string_1, string_2):
    #слова равны
    if string_1 == string_2:
        return 0

    len_1 = len(string_1)
    len_2 = len(string_2)

    #одно из слов пустое
    if len_1 == 0:
        return len_2
    if len_2 == 0:
        return len_1

    #первое слово короче
    if len_1 > len_2:
        string_2, string_1 = string_1, string_2
        len_2, len_1 = len_1, len_2

    prev_cost = 0
    d0 = [i for i in range(len_2 + 1)]
    d1 = [j for j in range(len_2 + 1)]
    print(d0)
    dprev = d0[:]

    s1 = string_1
    s2 = string_2

    for i in range(len_1):
        d1[0] = i + 1
        for j in range(len_2):
            cost = d0[j]

            if s1[i] != s2[j]:
                #замена
                cost += 1

                #вставка
                x_cost = d1[j] + 1
                if x_cost < cost:
                    cost = x_cost

                #удаление
                y_cost = d0[j + 1] + 1
                if y_cost < cost:
                    cost = y_cost

                #перестановка
                if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                    transp_cost = dprev[j - 1] + 1
                    if transp_cost < cost:
                        cost = transp_cost
            d1[j + 1] = cost

        
        dprev, d0, d1 = d0, d1, dprev
        print(d0)

    return d0[-1]

for i in range(1, 8):
    one = input()
    two = input()
    print(one, two)
    print(damerau_levenshtein(one, two))
