#Key:value data structure, hashmap
dic = {"Key1":"Value1","Key2":"Value2"}

print(dic["Key1"])
print(dic.get("Key1"))

#example
prices = {"Apple": 3.99, "Banana": 2.99,"Oranges": 4.99}

#can hold any objects pretty much
d = {"k1":2, "K2":[1,2,3], "K3":{"K1": 2}}
print(d["K2"][2])
print(d["K3"]["K1"])

#example change the list in a dic
d = {"K1": ['a','b','c']}
d["K1"][2] = d["K1"][2].upper()
d["K1"].append("d")
print(d)

#adding to a dic
d = {1:"Hello"}
d[2] = "Python"
d[1] = "olleH"
if 2 in d.keys():
    print(d)
else:
    print("Key is not in dictionary")

#access all keys in map
x = d.keys()

#access all values
y = d.values()

#get all items
z = d.items()

print(f"All Keys: {x}\nAll Values: {y}\nAll items: {z}")
