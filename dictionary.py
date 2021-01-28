d1 = {"Harry":"Burger", "Ron":"Fish", "Hermony":"Roti",
"Dumbeldoor":{"B":"Maggie", "L":"Biriani","D":"Chicken"}}
d1 ["Navill"] = "Junk Food"
d1 ["Voldemot"] = "Flesh"
d1[420] = "Habijabi"
print(d1)
print(d1["Harry"])
print(d1["Dumbeldoor"])
print(d1["Dumbeldoor"]["B"])
del d1[420]
print(d1)
d2 = d1.copy()
del d1["Harry"]
print(d1)
d1.update({"Chow":"Toffee"})
print(d1)
print(d1.items())