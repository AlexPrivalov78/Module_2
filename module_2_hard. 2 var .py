n = int(input("Введите число от 3 до 20: "))
numbers = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]
pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] != numbers[j]:
            pair = str(numbers[i]) + str(numbers[j])
            pairs.append(pair)
result = ""
for pair in pairs:
    if int(pair) % n == 0:
        result += pair
print("Нужный пароль:", result)