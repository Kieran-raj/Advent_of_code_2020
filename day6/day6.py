with open('test.txt', 'r') as f:
    lines = [line.replace(r'\n', ' ') for line in f.readlines()]
    lines = [line.strip() for line in lines]
    
def part_one(lines):
    lines = ''.join([line.replace('', ' ') if len(line) == 0 else line for line in lines])
    groups = lines.split()
    count = 0
    for group in groups:
        dic = {}
        for char in group: 
            if char not in dic.keys():
                dic[char] = 0
                dic[char] += 1
        count += sum(dic.values())
    return count


def part_two(lines):
    count = 0
    dic = {}
    lst_dics = []
    for i in lines:
        length_group = 0
        if i == '':
            dic = {}            
        for char in i:
            length_group += 1
            if char not in dic.keys():
                dic[char] = 1
            else:
                dic[char] += 1
        print('length of group',length_group)
        print(dic)
        print('length of dic', len(dic))
         


#print(part_one(lines))
part_two(lines)
print(lines)

