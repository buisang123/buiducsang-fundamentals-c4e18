# person = ["quy",20,0,"vinh phuc",2,["manga","coding"],3,20]

# dictionary
person = {
    "name": "quy","age": 20,"ex": 0
}    #key : value
# print(person)

# name = person["name"]
# print(name)
person["lenght"] = 20
# print(person)

person['lenght'] = 10
# del person["lenght"]


# key = 'lenght'
# if key in person:

#     # print(person[key])
# else:
#     # print("not found")

# for k in person:
#     print(k,person[k])

for k,v in person.items():
    print(k,v)