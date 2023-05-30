import json

file1 = open('records.txt', mode='r')

file2 = open('record2.txt', mode='w')

with file1, file2:
    for record in file1:
        sn, name, score = record.split()
        if sn != "007":
            file2.write(record)
        else:
            new_record = ' '.join([sn, "Johnson", score])
            file2.write(new_record + "\n")

# with open("records.txt", mode='a') as file:
#     file.write("\n009 Peter Pan 75\n")
#     file.write("010 James Bond 75\n")


record = {"student-records": [
    {"id": 1, "name": "ebuka", "age": 41},
    {"id": 2, "name": "dele", "age": 44},
    {"id": 3, "name": "sultan", "age": 31},
]}


with open("record.jason", mode="w") as rec:
    json.dump(record, rec)

with open("record.jason", mode='r') as rec2:
    print(json.dumps(json.load(rec2), indent=4))