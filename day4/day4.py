import re

def format_input():
    with open('input2.txt', 'r') as f:
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


def is_valid(passport):
    byr_range = range(1920, 2003)
    iyr_range = range(2010, 2021)
    eyr_range = range(2020, 2030)
    hgt_cm_range = range(150, 194)
    hgt_in_range = range(59, 77)
    hcl = re.compile('#[0-9][a-f][0-9][a-f][0-9][a-f][0-9][a-f][0-9][a-f][0-9][a-f]')
    ecl_range = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    #pid = re.match("0000[0-9]+")
    return passport


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
        print(is_valid(people))

    #valid = 0
    #for people in all_people:
    #    if len(people) == 8:
    #        valid += 1
    #    elif len(people) == 7 and 'cid' not in people.keys():
    #            valid += 1
    #return valid


lst = format_input()
func(lst)

