from puzzle import Puzzle
from queue import LifoQueue
import copy


class HillClimbing:
    @staticmethod
    def solve(x_in, window):
        pop, trial = Puzzle(), Puzzle()
        trial.init(x_in, "")
        stack = LifoQueue()
        stack.put(copy.deepcopy(trial))
        is_searched = {trial.id: True}
        if trial.is_target():
            return trial.path

        while not stack.empty():
            window.update()
            pop = stack.get()
            sx = int(pop.space % Puzzle.N)
            sy = int(pop.space / Puzzle.N)

            node_list = []
            # search for node
            for r in range(4):
                tx = sx + Puzzle.dx[r]
                ty = sy + Puzzle.dy[r]
                if tx < 0 or ty < 0 or tx >= Puzzle.N or ty >= Puzzle.N:
                    continue
                trial.init(pop.x, pop.path)
                trial.swap(trial.space, tx + ty * Puzzle.N)
                if trial.id not in is_searched.keys():

                    trial.path = trial.path + Puzzle.dir[r]
                    node_list.append(copy.deepcopy(trial))

                    is_searched[trial.id] = True
                    if trial.is_target():
                        return trial.path

            # sort
            for i in range(len(node_list) - 1):
                for j in range(i + 1, len(node_list) - 1)[::-1]:
                    if node_list[j].f() < node_list[j - 1].f():
                        node_list[j], node_list[j - 1] = \
                            copy.deepcopy(node_list[j - 1]), copy.deepcopy(node_list[j])

            # push into stack 最好的最后放进去
            for l in node_list:
                stack.put(copy.deepcopy(l))



