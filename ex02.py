def calc_manual_sum(*nums):
    total = 0
    for num in nums:
        total += num
    print(total)
    return total


calc_manual_sum(1, 2, 3)
calc_manual_sum(*[1, 2, 3])
