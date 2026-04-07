def max_subarray_sum(arr):
    if not arr:
        return 0
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def main():
    test_cases = [
        [1],
        [-5, -2, -1, -4],
        [5, 4, -1, 7, 8],
        []
    ]
    for arr in test_cases:
        result = max_subarray_sum(arr)
        print(f"Массив: {arr}")
        print(f"Максимальная сумма подмассива: {result}\n")


if __name__ == "__main__":
    main()