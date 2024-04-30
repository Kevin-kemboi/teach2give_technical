def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num

print(reverse_integer(500))
print(reverse_integer(-56))
print(reverse_integer(-90))
print(reverse_integer(91))
