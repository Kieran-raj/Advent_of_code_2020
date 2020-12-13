import math


def get_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    lines_lst = [i.strip() for i in lines]

    return lines_lst


def row_column():
    passes = get_input('input.txt')

    final_values = []

    for pass_ in passes:
        row_start = 0
        row_end = 128
        for i in pass_[:7]:
            ranges = range(int(row_start), int(row_end))
            if i == 'F':
                row_end -= len(ranges) // 2
            elif i == 'B':
                row_start += len(ranges) // 2 
            #print(ranges) 
        
        values = []

        if pass_[6] == 'F':
            values.append(min(ranges))
        else:
            values.append(max(ranges))
        col_start = 0
        col_end = 8
        #print(pass_[7:])
        for i in pass_[7:]:
            ranges = range(int(math.ceil(col_start)), int(col_end))
            if i == 'R':
                col_start += len(ranges) / 2
            elif i == 'L':
                col_end -= len(ranges) / 2
            #print(ranges)
        if pass_[9] == 'R':
            values.append(max(ranges))
        else:
            values.append(min(ranges))
        
        final_values.append(values)

    return final_values


all_values = row_column()
answers = []
for i in all_values:
    ans = (i[0] * 8) + i[1]
    answers.append(ans)


print(max(answers))







