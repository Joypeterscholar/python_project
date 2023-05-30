def set_unique_nums(my_list):
    sum_first_list = 0
    sum_unique_list = 0
    sum_of_both_list = 0
    unique_list = []
    for i in range(len(my_list)):
        sum_first_list = sum_first_list + my_list[i]
        num = i
        if my_list[i] == num and my_list[i] == num:
            unique_list.append(my_list[i])

    for i in unique_list:
        sum_unique_list = sum_unique_list + i
        sum_of_both_list = sum_first_list - sum_unique_list

    if sum_of_both_list % 2 !=0:
        res = my_list
    else:
        res = unique_list
    return res
print(set_unique_nums([2,2,4,6]))
