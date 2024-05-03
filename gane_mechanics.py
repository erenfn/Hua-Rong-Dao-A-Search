def can_move_left(blocks_dic: dict, pos_dic1: dict, number: int) -> bool:
    for pos in pos_dic1[number]:
        if pos % 4 == 0 or not (blocks_dic[pos - 1] == 0 or blocks_dic[pos - 1] == blocks_dic[pos]):
            return False
    return True


def move_left(blocks_dic: dict, pos_dic1: dict, number: int):
    i = 0
    for pos in pos_dic1[number]:
        blocks_dic[pos - 1] = number
        blocks_dic[pos] = 0

        pos_dic1[number][i] = pos - 1
        pos_dic1[0].remove(pos - 1)
        pos_dic1[0].append(pos)
        i += 1

    return blocks_dic, pos_dic1


def can_move_right(blocks_dic: dict, pos_dic1: dict, number: int) -> bool:
    for pos in pos_dic1[number]:
        if pos % 4 == 3 or not (blocks_dic[pos + 1] == 0 or blocks_dic[pos + 1] == blocks_dic[pos]):
            return False
    return True


def move_right(blocks_dic: dict, pos_dic1: dict, number: int):
    for i in range(len(pos_dic1[number]) - 1, -1, -1):
        pos = pos_dic1[number][i]
        blocks_dic[pos + 1] = number
        blocks_dic[pos] = 0

        pos_dic1[number][i] = pos + 1
        pos_dic1[0].remove(pos + 1)
        pos_dic1[0].append(pos)

    return blocks_dic, pos_dic1


def can_move_up(blocks_dic: dict, pos_dic1: dict, number: int) -> bool:
    for pos in pos_dic1[number]:
        if pos // 4 == 0 or not (
                blocks_dic[pos - 4] == 0 or blocks_dic[pos - 4] == blocks_dic[pos]):
            return False
    return True


def move_up(blocks_dic: dict, pos_dic1: dict, number: int):
    i = 0
    for pos in pos_dic1[number]:
        blocks_dic[pos - 4] = number
        blocks_dic[pos] = 0

        pos_dic1[number][i] = pos - 4
        pos_dic1[0].remove(pos - 4)
        pos_dic1[0].append(pos)
        i += 1

    return blocks_dic, pos_dic1


def can_move_down(blocks_dic: dict, pos_dic1: dict, number: int) -> bool:
    for pos in pos_dic1[number]:
        if pos // 4 >= 4 or not (
                blocks_dic[pos + 4] == 0 or blocks_dic[pos + 4] == blocks_dic[pos]):
            return False
    return True


def move_down(blocks_dic: dict, pos_dic1: dict, number: int):
    for i in range(len(pos_dic1[number]) - 1, -1, -1):
        pos = pos_dic1[number][i]
        blocks_dic[pos + 4] = number
        blocks_dic[pos] = 0

        pos_dic1[number][i] = pos + 4
        pos_dic1[0].remove(pos + 4)
        pos_dic1[0].append(pos)

    return blocks_dic, pos_dic1


class Piece:
    def __init__(self, top_left):
        self.top_left = top_left

    def move_left(self):
        self.top_left -= 1

    def move_right(self):
        self.top_left += 1

    def move_up(self):
        self.top_left -= 4

    def move_down(self):
        self.top_left += 4

    def can_move_left(self) -> bool:
        pass

    def can_move_right(self) -> bool:
        pass

    def can_move_up(self) -> bool:
        pass

    def can_move_down(self) -> bool:
        pass


class VerticalPiece(Piece):
    pass


def execute_move(direction, blocks_dic, pos_dic, number):
    if direction == 'left':
        return move_left(blocks_dic, pos_dic, number)
    elif direction == 'right':
        return move_right(blocks_dic, pos_dic, number)
    elif direction == 'up':
        return move_up(blocks_dic, pos_dic, number)
    elif direction == 'down':
        return move_down(blocks_dic, pos_dic, number)
    else:
        raise ValueError("Invalid direction")


def possible_moves(blocks_dic: dict, pos_dic: dict) -> dict:
    possible_left = []
    possible_right = []
    possible_up = []
    possible_down = []

    for number in pos_dic.keys():
        if can_move_up(blocks_dic, pos_dic, number):
            possible_up.append(number)
        if can_move_down(blocks_dic, pos_dic, number):
            possible_down.append(number)
        if can_move_right(blocks_dic, pos_dic, number):
            possible_right.append(number)
        if can_move_left(blocks_dic, pos_dic, number):
            possible_left.append(number)

    return {'left': possible_left, 'right': possible_right, 'up': possible_up, 'down': possible_down}


def goal_state(pos_dict):
    return pos_dict[1][0] == 13


def pos_to_list(pos_dict):
    sorted_values = [pos_dict[key] for key in sorted(pos_dict.keys())]
    return '-'.join(map(str, sorted_values))


def pos_to_new_dict(pos_dic):
    new_dict = {}
    for key in pos_dic.keys():
        num = pos_dic[key]
        if num >= 7:
            new_dict[key] = 4
        elif num in range(2, 7):
            if pos_dic[num][0] == pos_dic[num][1] + 1 or pos_dic[num][0] == pos_dic[num][1] - 1:
                new_dict[key] = 2
            else:
                new_dict[key] = 3
    return new_dict


def pos_to_new_list(pos_dic):
    sorted_values = []
    for key in sorted(pos_dic.keys()):
        num = pos_dic[key]
        if num >= 7:
            sorted_values.append(4)
        elif num in range(2, 7):
            if key + 1 in pos_dic and pos_dic[key] == pos_dic[key + 1]:
                sorted_values.append(2)
            elif num - 1 in pos_dic and pos_dic[num] == pos_dic[num - 1]:
                sorted_values.append(2)
            else:
                sorted_values.append(3)
        else:
            sorted_values.append(num)
    return ''.join(map(str, sorted_values))



