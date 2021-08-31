def calc_manual_sum(*nums, other=0):
    total = 0
    for num in nums:
        total += num
    if other:
        total += other
    print(total)
    return total


calc_manual_sum(1, 2, 3)
calc_manual_sum(*[1, 2, 3])
calc_manual_sum(1, 2, 3, other=1)
calc_manual_sum(*[1, 2, 3], other=1)
