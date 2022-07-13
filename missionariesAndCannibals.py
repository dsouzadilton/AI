#Missionaries and Cannibals problem
class MandC:

    def __init__(self):
        pass

    def solve(self, initial_missionaries, initial_cannibals):

        class States:
            def __init__(self, left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position):
                self.left_missionaries = left_missionaries
                self.left_cannibals = left_cannibals
                self.right_missionaries = right_missionaries
                self.right_cannibals = right_cannibals
                self.boat_position = boat_position
                self.parent = None
            #Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class
            def __eq__(self, other):
                return (self.left_missionaries == other.left_missionaries and self.left_cannibals == other.left_cannibals and
                        self.right_missionaries == other.right_missionaries and self.right_cannibals == other.right_cannibals and
                        self.boat_position == other.boat_position)
            #The goal state is 0 missionaries and cannibals on the left side and 3 missionaries and cannibals on the right side
            def goal_state(self):
                if self.left_missionaries == 0 and self.left_cannibals == 0 and self.right_missionaries == initial_missionaries \
                        and self.right_cannibals == initial_cannibals and self.boat_position == "right":
                    return True
                else:
                    return False
            #Invalid cases for this problem are
            #1.If there are more cannibals then missionaries on the left side or right side
            #2.If number of missionaries or cannibals is less than zero on the left side or right side
            def valid_state(self):
                if (self.left_missionaries != 0 and self.left_cannibals > self.left_missionaries) \
                        or (self.right_missionaries != 0 and self.right_cannibals > self.right_missionaries) \
                        or self.left_missionaries < 0 or self.left_cannibals < 0 or self.right_missionaries < 0 \
                        or self.right_cannibals < 0:
                    return False
                else:
                    return True

        def successors(curr_state):
            successor = []
            # Five possible moves: Move 2 Missionaries, or 2 Cannibals, or 1 M + 1 C, or 1 M only, or 1 C only
            possible_moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
            if curr_state.boat_position == "left":  # boat moves from left to right
                for move in possible_moves:
                    new_state = States(curr_state.left_missionaries - move[0], curr_state.left_cannibals - move[1],
                                       curr_state.right_missionaries + move[0], curr_state.right_cannibals + move[1], "right")
                    if new_state.valid_state():
                        successor.append(new_state)
                        new_state.parent = curr_state
            else:  # boat moves from right to left
                for move in possible_moves:
                    new_state = States(curr_state.left_missionaries + move[0], curr_state.left_cannibals + move[1],
                                       curr_state.right_missionaries - move[0], curr_state.right_cannibals - move[1], "left")
                    if new_state.valid_state():
                        successor.append(new_state)
                        new_state.parent = curr_state
            return successor

        def dfs():  # depth-first-search (DFS)
            initial_state = States(initial_missionaries, initial_cannibals, 0, 0, "left")  # root
            if initial_state.goal_state():
                return initial_state
            stack = []
            explored = []
            stack.append(initial_state)
            while stack:
                node = stack.pop()
                if node.goal_state():
                    return node
                explored.append(node)
                node_children = successors(node)
                for child in node_children:
                    if (child not in explored) and (child not in stack):
                        stack.append(child)
            return None
        #Storing the result in final path
        def find_moves(result):
            path = []
            final_path = []
            result_parent = result.parent
            while result_parent:
                move = (abs(result.left_missionaries - result_parent.left_missionaries),
                        abs(result.left_cannibals - result_parent.left_cannibals))
                path.append(move)
                result = result_parent
                result_parent = result.parent
            for i in range(len(path)):
                final_result = path[len(path) - 1 - i]
                final_path.append(final_result)
            return final_path

        solution = dfs()
        if solution:
            return find_moves(solution)
        else:
            return []
def main():
    t=MandC()
    print("Missionaries and Cannibals")
    if t.solve(3,3):
        print(t.solve(3,3))
    else:
        print("No solution found")
if __name__ == "__main__":
    main()
