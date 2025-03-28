import time

from model.LRUCache import LRUCache
import random

# NO CACHE
def range_sum_no_cache(array: list, L: int, R: int):
    length = len(array)
    if L > length or R > length or L > R or L < 0 or R < 0:
        return None
    sum = 0
    for el in array[L:R]:
        sum += el
    return sum

def update_no_cache(array: list, index: int, value) -> None:
    if len(array) > index >= 0:
        array[index] = value

# WITH CACHE
cache = LRUCache(1000)
def range_sum_with_cache(array: list, L: int, R: int):
    length = len(array)
    if L > length or R > length or L > R or L < 0 or R < 0:
        return None
    if (L, R) not in cache.cache:
        sum = 0
        for el in array[L:R]:
            sum += el
        cache.put((L, R), sum)
    return cache.get((L, R))

def update_with_cache(array: list, index: int, value) -> None:
    if len(array) > index >= 0:
        array[index] = value
        for (L, R) in list(cache.cache.keys()):
            if L <= index <= R:
                cache.remove((L, R))

if __name__ == "__main__":

    arr = []
    requests = []
    for i in range(100000):
        if i < 50000: # generating requests
            func = random.choice(["Range","Update"])
            if func == "Range":
                L = random.randint(0, 100000)
                R = random.randint(L, 100000)
                requests.append((func, L, R))
            else:
                index = random.randint(0, 100000)
                value = random.randint(-100, 100)
                requests.append((func, index, value))
        arr.append(random.randint(-100, 100)) # generating array


    # For NO CACHE
    start = time.time()
    for (func, i, j) in requests:
        if func == "Range":
            range_sum_no_cache(arr, i, j)
        else:
            update_no_cache(arr, i, j)
    exe_time_no_cache = time.time() - start

    # For WITH CACHE
    start = time.time()
    for (func, i, j) in requests:
        if func == "Range":
            range_sum_with_cache(arr, i, j)
        else:
            update_with_cache(arr, i, j)
    exe_time_with_cache = time.time() - start

    print(f"Час виконання без кешування: {exe_time_no_cache} секунд")
    print(f"Час виконання з LRU-кешем: {exe_time_with_cache} секунд")