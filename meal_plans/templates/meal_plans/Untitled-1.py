def names_in_list(names, people):
    index = 0
    new_list = []
    for n in names:
        if n == people[index]:
            result = True
        else:
            result = False
        new_list.append(result)
        index += 1
    return new_list


test = ["Steve", "Alex", "Josee", "Josh"]
test1 = ["Karla", "Alex", "Josee", "Ashley"]


print(names_in_list(test, test1))
