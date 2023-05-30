
#
# with open("student_records.txt", mode="a") as file:
#     file.write("06 Joseph Java\n")

with open("student_records.txt", mode="r") as file:
    print(file.read())
    print(file.close())

file1 = open("student_records.txt", mode="r")
file2 = open("records.txt", mode="w")

with file1, file2:
    for record in file1:
        number, name, language_of_choice = record.split()
        if number != "04":
            file2.write(record)
        else:
            new_record = " ".join([number, "Esther", language_of_choice])
            file2.write(new_record)
