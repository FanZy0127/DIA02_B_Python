number = -6523
sign = lambda num: 1 if num > 0 else -1

result = sign(number) * int(str(abs(number))[::-1])
print(result)
