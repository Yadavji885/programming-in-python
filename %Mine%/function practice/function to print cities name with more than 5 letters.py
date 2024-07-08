def city(cities):
    for i in cities.values():
        a = 0
        for j in i:
            a += 1
        if a > 6:
            ct = print(i)
    return ct
cities = {1 : "London",2 : "Jalandhar",3  : "Ludhiana",4 : "Mohali",5 : "Chandigarh"}
c = city(cities)