def find_divisible(max_range, divisibles):
    list_numbers = []
    for i in range(2, max_range):
        for d in divisibles:
            if i % d == 0:
                list_numbers.append(i)
                break
    return list_numbers


def sumList(array_list):
    sum = 0
    for i in array_list:
        sum += i
    return sum
