def bubble_sort(data: list) -> None:
    n = len(data)
    comparison_count = 0
    for i in range(n-1):
        for j in range(n-1):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j +1], data[j]
        print(f"End of pass {i}. `data` is now {data}")
    print(f"comparison_count is {comparison_count}")

def bubble_sort_opt(data: list) -> None:
    n = len(data)
    comparison_count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j +1], data[j]
        print(f"End of pass {i}. `data` is now {data}")
    print(f"comparison_count is {comparison_count}")

def bubble_sort_opt_more(data: list) -> None:
    n = len(data)
    comparison_count = 0
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j +1], data[j]
                swapped = True
        print(f"End of pass {i}. `data` is now {data}")
        if not swapped:
            break
    print(f"comparison_count is {comparison_count}")

# best case - already sorted
#numbers = [1, 2, 3, 4, 5, 6, 7] # when running this we're making n-1 comparisons, best case
numbers = [7, 6, 5, 4, 3, 2, 1] # worst case we make 21 comparisons, worst case
#numbers = [3, 2, 4, 1, 5, 7, 6]
#numbers = [1, 2, 3, 4, 6, 5, 7]
#numbers = list(range(70, 0, 1))

print(f"Sorting {numbers}")
bubble_sort_opt_more(numbers)
print(f"The sorted data is {numbers}")
