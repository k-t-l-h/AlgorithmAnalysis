from random import randint

def string_generator(n): 
    res = "" 

    for i in range(n):
        res += chr(randint(0, 25)+97)
    return res


def recursive_levenshtein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 1 and l2 == 1: 
        if s1 == s2:  
            return 0
        else:
            return 1
    else:
        if (l1 > l2 == 1) or (l2 > l1 == 1): 
            return abs(l1 - l2) + 1 

    t = 0
    if s1[-1] != s2[-1]: 
        t = 1

    return min(recursive_levenshtein(s1[:l1 - 1], s2) + 1,
               recursive_levenshtein(s1, s2[:l2 - 1]) + 1,
               recursive_levenshtein(s1[:l1 - 1], s2[:l2 - 1]) + t)


for i in range(99, 100):
    one = string_generator(i)
    two = string_generator(i)
    print(one, two)
    print(recursive_levenshtein(one, two))

