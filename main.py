import tkinter as tk
import time
import random
from dfs import DFS
from bfs import BFS
from best_first_search import BestFirstSearch
from hill_climbing import HillClimbing

puzzle_in = [i for i in range(9)]


def reset():
    global puzzle_in
    random.shuffle(puzzle_in)
    for i in range(9):
        if puzzle_in[i] == 0:
            arr_puzzle[i].config(text=str(""))
        else:
            arr_puzzle[i].config(text=str(puzzle_in[i]))
    btn_run.config(state=tk.NORMAL)
    label_find_the_result.config(text="Result:")
    label_time.config(text="Time:")
    label_steps.config(text="Steps:")
    print("Reset into: ", puzzle_in)


def run():
    label_find_the_result.config(text="Result:")
    label_time.config(text="Time:")
    label_steps.config(text="Steps:")
    btn_run.config(state=tk.DISABLED)
    btn_reset.config(state=tk.DISABLED)
    radio_dfs.config(state=tk.DISABLED)
    radio_bfs.config(state=tk.DISABLED)
    radio_bestfs.config(state=tk.DISABLED)
    radio_hc.config(state=tk.DISABLED)

    algorithm = alg.get()
    res = ""
    steps = 0
    time_start = time.time()
    if algorithm == 1:
        res = DFS.solve(puzzle_in, window)
        print("DFS: ", res)
    elif algorithm == 2:
        res = BFS.solve(puzzle_in, window)
        print("BFS: ", res)
    elif algorithm == 3:
        res = BestFirstSearch.solve(puzzle_in, window)
        print("Best First Search: ", res)
    elif algorithm == 4:
        res = HillClimbing.solve(puzzle_in, window)
        print("Hill Climbing: ", res)
    time_end = time.time()
    if res is None:
        solution = "No!"
    else:
        solution = "Yes!"
        steps = len(res)
    output(solution, time_end - time_start, steps)
    btn_run.config(state=tk.NORMAL)
    btn_reset.config(state=tk.NORMAL)
    radio_dfs.config(state=tk.NORMAL)
    radio_bfs.config(state=tk.NORMAL)
    radio_bestfs.config(state=tk.NORMAL)
    radio_hc.config(state=tk.NORMAL)


def output(result, t, steps):
    label_find_the_result.config(text="Result:\t    " + result)
    label_time.config(text="Time:\t    " + str(t)[0:5] + " (s)")
    label_steps.config(text="Steps:\t    " + str(steps))


window = tk.Tk()
window.title("8-Puzzle Solution (Written by 李悦新 201764621160)")
window.geometry("760x470+600+250")

btn_reset = tk.Button(text="Reset", font=("微软雅黑", 19), bg="grey", fg="yellow", command=reset)
btn_reset.place(x=50, y=380, width=170, height=50)

btn_run = tk.Button(text="Run", font=("微软雅黑", 19), bg="grey", fg="yellow", command=run)
btn_run.place(x=250, y=380, width=170, height=50)
btn_run.config(state=tk.DISABLED)

alg = tk.IntVar()
alg.set(1)
radio_dfs = tk.Radiobutton(window, font=("微软雅黑", 20), padx=20, variable=alg, value=1)
radio_dfs.config(text="DFS")
radio_dfs.place(x=480, y=20)
radio_bfs = tk.Radiobutton(window, font=("微软雅黑", 20), padx=20, variable=alg, value=2)
radio_bfs.config(text="BFS")
radio_bfs.place(x=480, y=90)
radio_bestfs = tk.Radiobutton(window, font=("微软雅黑", 20), padx=20, variable=alg, value=3)
radio_bestfs.config(text="Best First Search")
radio_bestfs.place(x=480, y=160)
radio_hc = tk.Radiobutton(window, font=("微软雅黑", 20), padx=20, variable=alg, value=4)
radio_hc.config(text="Hill Climbing")
radio_hc.place(x=480, y=230)

label_find_the_result = tk.Label(text="Result: ", font=("微软雅黑", 15))
label_find_the_result.place(x=500, y=300)
label_time = tk.Label(text="Time: ", font=("微软雅黑", 15))
label_time.place(x=500, y=350)
label_steps = tk.Label(text="Steps: ", font=("微软雅黑", 15))
label_steps.place(x=500, y=400)

arr_puzzle = [tk.Button() for i in range(9)]
x_offset = -1
y_offset = -1
for i in range(9):
    if i % 3 == 0:
        x_offset = 0
        y_offset = y_offset + 1
    arr_puzzle[i].config(text="NULL", font=("微软雅黑", 30), width=5, height=1, bg="white", bd=0)
    arr_puzzle[i].place(x=40 + 150 * x_offset, y=20 + 120 * y_offset)
    arr_puzzle[i].config(state=tk.DISABLED)
    x_offset = x_offset + 1

window.mainloop()
