def reverse(x: int) -> int:
    tmp = []
    pow_10 = 1
    sum = 0
    is_negative = False

    if x < 0:
        is_negative = True
        x = abs(x)

    while x // 10 != 0:  # 1
        tmp.append(x % 10)  # 3 2
        x = x // 10  # 12 1
        pow_10 *= 10  # 100 1000

    tmp.append(x)

    for i in tmp:
        sum += i * pow_10
        pow_10 /= 10

    if sum > 2 ** 31:
        return 0

    return -1 * int(sum) if is_negative == True else int(sum)

print(reverse(-345))
