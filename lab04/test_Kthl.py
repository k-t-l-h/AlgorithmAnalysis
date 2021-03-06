from comb_sort import comb_sort
from patience_sort import patience_sort
from barier_sort import barier_sort
from random import randint
from time import perf_counter_ns

def random_list_gen(a):
    return [randint(0, 1000) for x in range(a)]

def increasing_list_gen(a):
    return [i for i in range(a)]

def decreasing_list_gen(a):
    return [a-i for i in range(a)]

def sort_test(sort):
    for x in range(500, 5001, 500):
        print("N = {:d}".format(x))
        n = 100
        rlg = 0
        ilg = 0
        dlg = 0
        for i in range(n):
            rlist = random_list_gen(x)
            ilist = increasing_list_gen(x)
            dlist = decreasing_list_gen(x)
            
            time_b = perf_counter_ns()
            sort(rlist)
            rlg += perf_counter_ns() - time_b
            
            time_b = perf_counter_ns()
            sort(ilist)
            ilg += perf_counter_ns() - time_b
            
            time_b = perf_counter_ns()
            sort(dlist)
            dlg += perf_counter_ns() - time_b
        rlg /= (10**9*n)
        ilg /= (10**9*n)
        dlg /= (10**9*n)
        print("{0}".format(rlg))
        print("{0}".format(ilg))
        print("{0}".format(dlg))
        print("-----------")
    print()

print("Сортировка расчёской:")
sort_test(comb_sort)

print("Терпеливая сортировка:")
sort_test(patience_sort)

print("Метод прямых вставок с барьером:")
sort_test(barier_sort)

        
    
