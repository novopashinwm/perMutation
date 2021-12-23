import itertools as it


a = [2,4,5,6,9]
b = 18
comb = it.combinations(a, 3) # it.combinations если не хотите учитывать обратные перестановки
print(comb)

result = [i for i in comb if sum(i) == b]

print(result)