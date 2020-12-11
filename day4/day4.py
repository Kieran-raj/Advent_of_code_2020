import collections

def format_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    overall_list = []
    person = []
    for i in lines:
        if i != '\n':
            person.append(i)
        else:
            overall_list.append(person)
            person = []
    overall_list.append(person)
    return overall_list


def func(lst):
    all_people = []
    for i in lst:
        person_dict = {}
        for j in i:
            attr = j.split()
            for k in attr:
                dict_setup = k.split(':')
                person_dict[dict_setup[0]] = dict_setup[1]
        all_people.append(person_dict)
    
    valid = 0
    for people in all_people:
        if len(people) == 8:
            valid += 1
        elif len(people) == 7 and 'cid' not in people.keys():
                valid += 1
    return valid

lst = format_input()
print(func(lst))

