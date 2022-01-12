import itertools as it
def printSum(b, array, times):
    comb = it.combinations(array, times)  # it.combinations если не хотите учитывать обратные перестановки
    result = [i for i in comb if sum(i) == b]
    print(result)

a = [1,2,3,4,5,6,7,8,9]
b = 12
printSum(b, a, 3)