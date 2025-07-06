# dictionary is used to store data in key:value pair

info={
    "key":"value",
    "name":"mohit",
    "roll":3.14,
    "working":True,
    "name1":["radhika","lila","sakshi"],
    "tup":("rina","mina","sina")
}
print(info)
print(type(info))

# dictionary are unordered,mutebale,don't allow for duplicate key
print(info["name"])
print(info["tup"])

# change value of info

info["name"]="Hello World"
print(info)

# null-dic

nulldic={}
print(nulldic)
nulldic["name"]="Mohit Sankhyan"
print(nulldic)