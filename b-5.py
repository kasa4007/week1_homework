def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number


def find_minimum(numbers):
    minimum_number = numbers[0]
    for num in numbers:
        if num < minimum_number:
            minimum_number = num
    return minimum_number


def find_average(numbers):
    total = find_sum(numbers)
    count = len(numbers)
    return total // count


input_numbers = input("データを入力してください(スペース区切り) > ")  # 1 1 2 3 5 8 13 21
numbers = [int(num) for num in input_numbers.split()]

print("合計値:", find_sum(numbers))
print("最大値:", find_max(numbers))
print("最小値:", find_minimum(numbers))
print("平均値:", find_average(numbers))
