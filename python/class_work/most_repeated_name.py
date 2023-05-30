import statistics


def get_most_repeated_name(names: list):
    # name = statistics.mode(names)
    num = 0
    for i in names:
        num = names.count(i)
    return names[num]


print(get_most_repeated_name(["fjjf", "may", "may", "jay", "jay", "jay", "jay", "jay", "may"]))
