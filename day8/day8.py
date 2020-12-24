with open('input.txt', 'r') as f:
    moves = [i.strip() for i in f.readlines()]


def list_moves(moves):
    moves = [i.split() for i in moves]
    for i in (moves):
        sign = i[1][0]
        value = i[1][1:]
        i[1] = sign
        i.append(value)
        i.append(0)
    return calc(moves)


def calc(moves):
    count = 0
    idx = 0
    while moves[idx][3] == 0:
        if moves[idx][0] == 'nop':
            moves[idx][3] = 1
            idx += 1
        elif moves[idx][0] == 'acc':
            count = eval(f'count {moves[idx][1]} {moves[idx][2]}')
            moves[idx][3] = 1
            idx += 1
        elif moves[idx][0] == 'jmp':
            moves[idx][3] = 1
            idx = eval(f'idx {moves[idx][1]} {moves[idx][2]}')

    return count
        

print(list_moves(moves))