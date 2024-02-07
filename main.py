
import random

number = []

def bubble_sort(random_numbers):
    global number
    number = random_numbers[:]
    """Сортировка пузырьком"""
    n = len(number)
    for i in range(n):
        for j in range(0, n-i-1):
            if number [j] > number [j+1]:
                number [j], number [j+1] = number [j+1], number[j]
    return number


def insertion_sort(random_numbers):
    number = random_numbers[:]
    """Сортировка вставками"""
    for i in range(1, len(number)):
        key = number[i]
        j = i - 1
        while j >= 0 and key < number[j]:
            number[j + 1] = number[j]
            j -= 1
        number[j + 1] = key
    return number


def selection_sort(random_numbers):
    """Сортировка выбором"""
    numbers = random_numbers[:]  # Создаем копию списка
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers



# def quick_sort(random_numbers):
#     """Быстрая сортировка"""
#     if len(number) <= 1:
#         return number
#     pivot = number[len(number) // 2]
#     left = [x for x in number if x < pivot]
#     middle = [x for x in number if x == pivot]
#     right = [x for x in number if x > pivot]
#     number = quick_sort(left) + middle + quick_sort(right)
#     return number

#
# def merge_sort(random_numbers):
#     """Сортировка слиянием"""
#     if len(number) > 1:
#         mid = len(number) // 2
#         left_half = number[:mid]
#         right_half = number[mid:]
#
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         i = j = k = 0
#
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 number[k] = left_half[i]
#                 i += 1
#             else:
#                 number[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_half):
#             number[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             number[k] = right_half[j]
#             j += 1
#             k += 1
#     return number


#
# if __name__ == '__main__':
#     start_time = time.time()
#     sorted_number = sort_func(random_numbers)
#     end_time = time.time() - start_time
#     print(sorted_number)
#     print('Время: %s секунд' % end_time)