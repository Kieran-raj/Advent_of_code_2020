with open('input.txt', 'r') as f:
    lines = f.readlines()


def search_function(lst, line):
    index = line[0].find(' bags')
    bags = []
    for a in lst:
        if line[0][:index] in a[0] and a[0][:10] != line[0][:index]:
            bags.append(line[0][:index])
            # return 1
    print(set(bags))


def get_shiny_list(lines):
    list_of_lines = [[line.strip()] for line in lines]
    lines_with_shiny = []
    count = 0
    for a in list_of_lines:
        if 'shiny gold' in a[0] and a[0][:10] != 'shiny gold':
            count += 1
            lines_with_shiny.append(a)

    for i in lines_with_shiny:
        search_function(list_of_lines, i)
    # for line in lines_with_shiny:
    #     count += search_function(list_of_lines, line)
    
    # print(count)
    

get_shiny_list(lines)