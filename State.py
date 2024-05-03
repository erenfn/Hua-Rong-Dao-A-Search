class GameState:
    def __init__(self, blocks_dic, pos_dic, count, heuristic, parent=None):
        self.blocks_dic = blocks_dic  # Dictionary representing the blocks
        self.pos_dic = pos_dic  # Dictionary representing the positions
        self.count = count  # Counter for the number of moves
        self.heuristic = heuristic  # Heuristic function
        self.parent = parent

    def __lt__(self, nxt):
        return self.heuristic < nxt.heuristic
