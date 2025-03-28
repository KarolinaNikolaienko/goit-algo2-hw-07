from model.LRUCache import LRUCache


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

    arr = [1,2,3,4]
    print(range_sum_with_cache(arr, 1, 3))
    print(range_sum_with_cache(arr, 0, 4))
    print(cache.cache)
    update_with_cache(arr, 0, 9)
    print(arr)
    print(cache.cache)