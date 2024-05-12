import timeit
import random
import matplotlib.pyplot as plt

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Вимірюємо час сортування
def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    end_time = timeit.default_timer()
    return end_time - start_time

# Генеруємо різні набори даних для тестування
data_sets = {
    "Small": random.sample(range(100), 10),
    "Medium": random.sample(range(1000), 100),
    "Large": random.sample(range(10000), 1000)
}

# Зберігаємо часи виконання для кожного набору даних
merge_times = []
insertion_times = []
timsort_times = []

for name, data in data_sets.items():
    merge_times.append(measure_time(merge_sort, data))
    insertion_times.append(measure_time(insertion_sort, data))
    timsort_times.append(timeit.timeit(stmt='sorted(data)', globals=globals(), number=1))

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(list(data_sets.keys()), merge_times, label='Merge Sort')
plt.plot(list(data_sets.keys()), insertion_times, label='Insertion Sort')
plt.plot(list(data_sets.keys()), timsort_times, label='Timsort')
plt.xlabel('Розмір набору даних')
plt.ylabel('Час виконання (секунди)')
plt.title('Порівняння часу виконання сортування')
plt.legend()
plt.grid(True)
plt.show()
