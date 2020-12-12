import re

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


def is_valid(passport):
    tests = {'byr': range(1920, 2003), 
            'iyr': range(2010, 2021), 
            'eyr': range(2020, 2031), 
            'hgt': [range(150, 194), range(59, 77)], 
            'hcl': "^\#[0-9a-f]{6}$",
            'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
            'pid': "^\d{9}$"}
    true_params = 1
    test = []   
    for i in passport:
        if i in ['byr', 'iyr','eyr']:
            if passport[i] in tests[i]:
                true_params += 1
        elif i == 'hcl':
            if bool(re.fullmatch(tests['hcl'], passport[i])):
                true_params += 1
        elif i in tests['ecl']:
            true_params += 1
        elif i == 'pid':
            if bool(re.fullmatch(tests['pid'], passport[i])):
                true_params += 1
        elif i == 'hgt':
            if passport[i][1] == 'in':
                if passport[i][0] in tests[i][1]:
                    true_params += 1
            elif passport[i][1] == 'cm':
                if passport[i][0] in tests[i][0]:
                    true_params += 1
        elif i == 'cid':
            true_params += 1
        #print(f'lenth: {len(passport)}, true_params: {true_params}')
        #print(i, passport[i])
    if true_params == len(passport):
        test.append(passport)
        return True
    else:
        return False
     
    #for i in test:
    #    for j in i:
     #       print(j, i[j])


def change_types(passports):
    for passport in passports:
        for i in passport:
            if i in ['byr', 'iyr','eyr']:
                passport.update({i:int(passport[i])})
            if i == 'hgt':
                new = {}
                value_units = []
                try:
                    value_units.append(int(passport[i][:-2]))
                except ValueError:
                    value_units.append(None)
                value_units.append(passport[i][-2:])
                new = {'hgt': value_units}
                passport.update(new)
    
    return passports


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

    final_passports = change_types(all_people)

    for i in [p for p in final_passports if len(p) > 6]:
        #print('\n')
        #print(len(i))
        if len(i) == 8:
            if is_valid(i):
                valid += 1
        else:
            if 'cid' not in i.keys():
                if is_valid(i):
                    valid += 1

    return valid


lst = format_input()
print(func(lst))

