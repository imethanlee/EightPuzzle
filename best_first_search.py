from queue import PriorityQueue
from puzzle import Puzzle
import copy


class BestFirstSearch:
    @staticmethod
    def solve(x_in, window):
        pop, trial = Puzzle(), Puzzle()
        trial.init(x_in, "")
        trial.depth = 0
        q = PriorityQueue()
        q.put(copy.deepcopy(trial))
        is_searched = {trial.id: True}
        if trial.is_target():
            return trial.path

        while not q.empty():
            window.update()
            pop = q.get()
            sx = int(pop.space % Puzzle.N)
            sy = int(pop.space / Puzzle.N)
            for r in range(4):
                tx = sx + Puzzle.dx[r]
                ty = sy + Puzzle.dy[r]
                if tx < 0 or ty < 0 or tx >= Puzzle.N or ty >= Puzzle.N:
                    continue
                trial.init(pop.x, pop.path)
                trial.set_depth(pop.depth + 1)
                trial.swap(trial.space, ty * Puzzle.N + tx)
                if trial.id not in is_searched.keys():
                    is_searched[trial.id] = True
                    trial.path = trial.path + Puzzle.dir[r]
                    if trial.is_target():
                        return trial.path
                    q.put(copy.deepcopy(trial))
