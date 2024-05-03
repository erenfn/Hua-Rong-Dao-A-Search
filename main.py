import copy
import heapq
import io_manager as io
import gane_mechanics as gm
import time
from State import GameState


def a_star(blocks_dic: dict, pos_dic: dict):
    start_time = time.time()
    start_state = GameState(blocks_dic, pos_dic, 0, 0)
    heap = []
    heapq.heappush(heap, start_state)
    visited = set()

    while heap:
        gs = heapq.heappop(heap)
        count = gs.count
        current_pos_dic = gs.pos_dic
        current_blocks_dic = gs.blocks_dic

        if gm.goal_state(current_pos_dic):  # Implement the goal_state function in game_mechanics.py
            io.output_to_file('output.txt', count, gs)
            print(time.time() - start_time)
            return True  # Puzzle solved

        if gm.pos_to_new_list(current_blocks_dic) in visited:
            continue

        visited.add(gm.pos_to_new_list(current_blocks_dic))

        # Generate successor states
        for direction in ['left', 'right', 'up', 'down']:
            for move in gm.possible_moves(current_blocks_dic, current_pos_dic)[direction]:
                new_blocks_dic, new_pos_dic = gm.execute_move(direction, copy.deepcopy(current_blocks_dic),
                                                              copy.deepcopy(current_pos_dic), move)
                if gm.pos_to_new_list(new_blocks_dic) not in visited:
                    new_state = GameState(new_blocks_dic, new_pos_dic, count + 1, count + 1 + heuristic(new_pos_dic),gs)
                    heapq.heappush(heap, new_state)

    return False  # No solution found


def distance_btw_sol(i: int) -> int:
    return abs(3 - i // 4) + abs(i % 4 - 1)


def heuristic(pos_dict) -> int:
    return 50 * distance_btw_sol(pos_dict[1][0])


if __name__ == '__main__':
    # if len(sys.argv) != 4:
    #     print("length of sysargv should be 4")
    #     exit(1)
    # input = 'inputs/' + sys.argv[1]

    input = "inputs/input3.txt"

    blocks_dic = {}  # position to blocks
    pos_dic = {}  # blocks to poistions
    io.input_read(input, blocks_dic, pos_dic)

    result = a_star(blocks_dic, pos_dic)
    if result:
        print('Puzzle Solved')
    else:
        print('Failed to solve the puzzle')
