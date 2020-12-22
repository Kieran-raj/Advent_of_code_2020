with open('input.txt', 'r') as f:
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
    lines = ('_'.join([line if len(line) == 0 else line for line in lines])).split('__')
    use = [[i] for i in lines]
    count = 0
    for i in use:
        num_groups = 1
        for j in i:
            num_groups += j.count('_')
            dic = {}
            for char in j:
                if char not in dic.keys():
                    if char != '_':
                        dic[char] = 0
                        dic[char] += 1 
                else:
                    dic[char] += 1
            for letter in dic:
                if dic[letter] == num_groups:
                    count += 1
    print(count)                        
            
             


#print(part_one(lines))
part_two(lines)

