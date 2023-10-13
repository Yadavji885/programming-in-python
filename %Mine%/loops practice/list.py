l1 = [29,14,56,88,99,956,45,74,77]
for i in l1:
    index = 0
    if i%7 == 0:
        index = l1.index(i)
        l1.remove(i)
        l1.insert(index,0)

print(l1)
