names: list[str] = ["names", "Ada", "Kemi", "zzzz"]
max_name: str = names[0]
for i in range(len(names)):
    if len(names[i]) >= len(max_name):
        max_name = names[i]
result: tuple = (max_name, len(max_name))
print(result)
