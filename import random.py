import random
import time


def quick_sort(array: list[float], ascending: bool = True) -> list[float]:
    if array is None:
        return []

    arr = array.copy()
    _quick_sort_recursive(arr, 0, len(arr) - 1, ascending)
    return arr


def _quick_sort_recursive(
    arr: list[float], low: int, high: int, ascending: bool
):
    if low < high:
        pivot_index = _partition(arr, low, high, ascending)
        _quick_sort_recursive(arr, low, pivot_index - 1, ascending)
        _quick_sort_recursive(arr, pivot_index + 1, high, ascending)


def _partition(
    arr: list[float], low: int, high: int, ascending: bool
) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if ascending:
            condition = arr[j] <= pivot
        else:
            condition = arr[j] >= pivot

        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def is_sorted(array: list[float], ascending: bool = True) -> bool:
    if not array or len(array) <= 1:
        return True

    for i in range(len(array) - 1):
        if ascending:
            if array[i] > array[i + 1]:
                return False
        else:
            if array[i] < array[i + 1]:
                return False
    return True


def generate_random_array(size: int) -> list[float]:
    return [round(random.uniform(-100.0, 100.0), 2) for _ in range(size)]


if __name__ == "__main__":
    sizes = [1_000, 10_000, 100_000]

    for size in sizes:
        print("=" * 50)
        print(f"Розмір масиву: {size} елементів")
        print("=" * 50)

        test_array = generate_random_array(size)

        start_time = time.perf_counter()
        sorted_asc = quick_sort(test_array, ascending=True)
        elapsed_asc = (time.perf_counter() - start_time) * 1000

        is_asc_correct = is_sorted(sorted_asc, ascending=True)
        print(
            f"За зростанням: Час = {elapsed_asc:.2f} ms | Відсортовано: {is_asc_correct}"
        )

        start_time = time.perf_counter()
        sorted_desc = quick_sort(test_array, ascending=False)
        elapsed_desc = (time.perf_counter() - start_time) * 1000

        is_desc_correct = is_sorted(sorted_desc, ascending=False)
        print(
            f"За спаданням:  Час = {elapsed_desc:.2f} ms | Відсортовано: {is_desc_correct}\n"
        )