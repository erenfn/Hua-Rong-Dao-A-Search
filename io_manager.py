import sys
from State import GameState


def input_read(input: str, blocks_dic: dict, post_dic: dict) -> None:
    with open(input) as f:
        lines = f.readlines()
        count = 0
        single_count = 1
        for line in lines:
            splitted = []
            splitted[:] = line

            for num in range(0, 4):
                number = int(splitted[num])
                if number == 7:
                    number += single_count
                    single_count += 1

                blocks_dic[count * 4 + num] = number
                if number not in post_dic.keys():
                    post_dic[number] = [count * 4 + num]
                else:
                    post_dic[number].append(count * 4 + num)

            if count >= 4:
                break
            count += 1


def write_output(blocks_dic: dict) -> str:
    output = ''
    for i in range(0, 5):
        for j in range(0, 4):
            key = j + i * 4
            num = blocks_dic[key]
            if num >= 7:
                num = 4
            elif num in range(2, 7):
                if key + 1 in blocks_dic and blocks_dic[key] == blocks_dic[key + 1]:
                    num = 2
                elif key - 1 in blocks_dic and blocks_dic[key] == blocks_dic[key - 1]:
                    num = 2
                else:
                    num = 3
            output += str(num)
    return output


def output_to_file(filename: str, count, state: GameState) -> None:
    main_out = sys.stdout
    f = open(filename, 'w')
    sys.stdout = f
    print("Cost of the solution:" + str(count))

    # new_state = state
    # while new_state.parent is not None:
    #     output = write_output(new_state.blocks_dic)
    #     for s in range(0, 6):
    #         print(output[s * 4:(s + 1) * 4])
    #     print('')
    #     new_state = new_state.parent

    new_state = state
    state_list = []
    while new_state.parent is not None:
        state_list.append(new_state)
        new_state = new_state.parent
    state_list.reverse()
    for state in state_list:
        output = write_output(state.blocks_dic)
        for s in range(0, 6):
            print(output[s * 4:(s + 1) * 4])
        print('')

    sys.stdout = main_out
    f.close()
