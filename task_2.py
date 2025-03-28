import timeit
from functools import lru_cache

from matplotlib import pyplot as plt
from tabulate import tabulate

from model.SplayTree import SplayTree

# from pybst.splaytree import SplayTree

@lru_cache(maxsize=128)
def fibonacci_lru(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

def fibonacci_splay(n: int, tree: SplayTree) -> int:
    data = tree.find(n)
    if data is None:
        if n <= 1:
            tree.insert(n, n)
            return n
        val = fibonacci_lru(n - 1) + fibonacci_lru(n - 2)
        tree.insert(n, val)
        return val
    else:
        return data

def draw_plot(x, yLRU, yTree):
    fig, ax = plt.subplots()

    ax.plot(x, yLRU, 'o-', linewidth=2, label="LRU Cache")
    ax.plot(x, yTree, 'o-', linewidth=2, color="orange", label="Splay Tree")

    plt.ylabel("Сереній час виконання (секунди)")
    plt.xlabel("Число Фібоначчі (n)")
    plt.title("Порівняння часу виконання для LRU Cache та Splay Tree")

    plt.grid(True)
    ax.legend(loc='upper right')

    plt.show()

if __name__ == "__main__":
    splayTree = SplayTree()
    fibonacci = []
    for num in range(0, 950 + 1, 50):
        fibonacci.append(num)

    SETUP_CODE = '''
from __main__ import splayTree, fibonacci_lru, fibonacci_splay
from functools import lru_cache
from model.SplayTree import SplayTree'''

    fibonacci_lru_res = []
    fibonacci_splay_res = []
    colomns = []
    for num in fibonacci:
        lru_res = timeit.timeit(setup=SETUP_CODE,
                                stmt=f"fibonacci_lru({num})")
        splay_res = timeit.timeit(setup=SETUP_CODE,
                                  stmt=f"fibonacci_splay({num}, splayTree)")
        fibonacci_lru_res.append(lru_res)
        fibonacci_splay_res.append(splay_res)
        colomns.append([num, lru_res, splay_res])

    # print(fibonacci_lru_res)
    # print(fibonacci_splay_res)
    print(tabulate(colomns, headers=["n", "LRU Cache Time (s)", "Splay Tree Time (s)"]))
    draw_plot(fibonacci, fibonacci_lru_res, fibonacci_splay_res)