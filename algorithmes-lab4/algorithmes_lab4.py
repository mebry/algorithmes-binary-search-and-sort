import datetime
import random, string
import time
import matplotlib.pyplot as plt

class Data(object):
    def __init__(self, _str, _time, _int):
        self.str = _str
        self.time = _time
        self.int = _int


class CheckSort(object):
    def __init__(self, _arr):
        self.arr = _arr
        self.fact = None

def binary_search(arr, key):
    start_element = 0
    end_element = len(arr) - 1
    while start_element <= end_element:
        middle_index = start_element + (end_element - start_element) // 2
        if (
            arr[middle_index].str == key.str
            and arr[middle_index].time == key.time
            and arr[middle_index].int == key.int
        ):
            return middle_index
        elif arr[middle_index].str < key.str:
            start_element = middle_index + 1
        else:
            end_element = middle_index - 1
    return -1


def random_str(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def random_int(a, b):
    return random.randint(a, b)


def random_time():
    # кол-во секунд в день: 86400
    rtime = int(random.random() * 86400)

    hours = int(rtime / 3600)
    minutes = int((rtime - hours * 3600) / 60)
    seconds = rtime - hours * 3600 - minutes * 60

    time_string = '%02d:%02d:%02d' % (hours, minutes, seconds)
    return time_string

def fourth_sort(check, key1=["str"]):
        if check.fact is None or check.fact < datetime.datetime.now():
            arr = check.arr
            selection_sort(arr, key1)
            check.fact = datetime.datetime.now()

def binary_search(arr, key):
        start_element = 0
        end_element = len(arr) - 1
        while start_element <= end_element:
            middle_index = start_element + (end_element - start_element) // 2
            if arr[middle_index].str == key.str and arr[middle_index].time == key.time and arr[middle_index].int == key.int:
                return middle_index
            elif arr[middle_index].str < key.str:
                start_element = middle_index + 1
            else:
                end_element = middle_index - 1
        return -1

def time4S(t):
    if (t>1000000000): return str(round(t/1000000000)) + ' s'
    if (t > 1000000): return str(round(t / 1000000)) + ' ms'
    if (t>1000): return str(round(t/1000)) + ' mks'
    return str(t) + ' ns'

def selection_sort(array, keys=[]):
    comp_count = 0
    swap_count = 0
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            # Сравниваем текущий минимум с элементом на j-ой позиции
            for k in keys:
                comp_count += 1
                if getattr(array[j], k) < getattr(array[min_idx], k):
                    min_idx = j
                    break
                elif getattr(array[j], k) > getattr(array[min_idx], k):
                    break
        if min_idx != i:
            #минимальный элемент находится не на позиции i, меняем его местами с элементом на позиции i
            array[i], array[min_idx] = array[min_idx], array[i]
            swap_count += 1  # увеличиваем количество перестановок для первого ключа
            if len(keys)!=1 and getattr(array[i], keys[1]) != getattr(array[min_idx], keys[1]):
                swap_count += 1  # увеличиваем количество перестановок для второго ключа
            if len(keys)==3 and getattr(array[i], keys[2]) != getattr(array[min_idx], keys[2]):
                swap_count += 1
    print(f'Number of comparisons: {comp_count}')
    print(f'Number of permutations: {swap_count}')

def fill_array(N):
    i = 0
    while i < N:
        str = random_str(random_int(1, 5))
        time = random_time()
        int = random_int(0, 9)

        new_object = Data(str, time, int)
        array.append(new_object)
        i += 1

def print_array(arr):
    i = 0
    while i < len(arr):
        print(arr[i].str, arr[i].int,arr[i].time)
        i += 1
    print()

array = []

fill_array(2000)

array1 = array.copy()
array2 = array.copy()
array3 = array.copy()
array4 = array.copy()

time_arr = []

t_start = time.perf_counter()
selection_sort(array1,['str'])
t_end = time.perf_counter()
time_arr.append(t_end - t_start)
print("Time to sort by one key:", time4S(time_arr[0]))

t_start = time.perf_counter()
selection_sort(array2,['str', 'int'])
t_end = time.perf_counter()
time_arr.append(t_end - t_start)
print("Time to sort by two keys:", time4S(time_arr[1]))

t_start = time.perf_counter()
selection_sort(array3,['str', 'int', 'time'])
t_end = time.perf_counter()
time_arr.append(t_end - t_start)
print("Time to sort by three keys:", time4S(time_arr[2]))

check = CheckSort(array4)
t_start = time.perf_counter()
fourth_sort(check, ["str"])
t_end = time.perf_counter()
print("Time to perform sorting with checks:", time4S(t_end - t_start))

find_element = array1[3]

t_start = time.perf_counter()
binary_search(array1, find_element)
t_end = time.perf_counter()
print("Binary search execution time:", time4S(t_end - t_start))

key_count_arr = [1, 2, 3]

plt.plot(key_count_arr, time_arr, marker='o')
plt.xlabel("key")
plt.ylabel("t")
plt.grid()
plt.show()