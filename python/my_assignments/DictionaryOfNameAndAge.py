people = [{"name": "Victor", "age": 21}, {"name": "Bright", "age": 19}, {"name": "Ebuka", "age": 22}]
people.append({"name":"John", "age": 28})
print(people)

name = input("Enter your name: ")
result = ''
for i in people:
    if name.__eq__(i["name"]):
        result = (f"Hello {i['name']}, you are {i['age']} years old")
# if
print(result)


# elif name == i['name']:
#     print((f"Hello {i['name']}, you are {i['age']} years old"))
#
# elif name == i['name']:
#     print((f"Hello {i['name']}, you are {i['age']} years old"))
# elif name != i['name']:
#     print(f"Name is not saved in database\n")
#     age = int(input("Enter age "))
#     people.append({"name":name, "age":age})
#     break

    # match name:
    #     case "Victor":
    #         result = (f"Hello {i['name']}, you are {i['age']} years old")
    #         break
    #     case "Bright":
    #         result = (f"Hello {i['name']}, you are {i['age']} years old")
    #         break
    #     case "Ebuka":
    #         result = (f"Hello {i['name']}, you are {i['age']} years old")
    #         break
