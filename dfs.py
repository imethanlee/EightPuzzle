from puzzle import Puzzle
from queue import LifoQueue
import copy


class DFS:
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
            for r in range(4):
                tx = sx + Puzzle.dx[r]
                ty = sy + Puzzle.dy[r]
                if tx < 0 or ty < 0 or tx >= Puzzle.N or ty >= Puzzle.N:
                    continue
                trial.init(pop.x, pop.path)
                trial.swap(trial.space, tx + ty * Puzzle.N)
                if trial.id not in is_searched.keys():
                    is_searched[trial.id] = True
                    trial.path = trial.path + Puzzle.dir[r]
                    if trial.is_target():
                        return trial.path
                    stack.put(copy.deepcopy(trial))
