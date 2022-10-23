def binary_search(b, x):
    shift = 0
    while len(b) > 0:
        i = len(b) // 2
        if b[i] == x:
            c = "Введённое число найдено, номер в возрастающей последовательности: " + str(shift + i + 1) + ", индекс: " + str(shift + i)
            return c
        if x < b[i]:
            b = b[:i]
        else:
            b = b[i+1:]
            shift += i + 1
    c = "Введённое число не найдено"
    return c

while True:
    a = list(map(int, input("Введите не повторяющиеся целые числа в произвольном порядке (они будут автоматически отсортированы по возрастанию), используя для их разделения пробелы, или введите 0 для выхода из программы: ").split()))
    if len(a) == 1 and a[0] == 0:
        break
    a.sort()
    x = int(input("Введите искомое число: "))
    print(binary_search(a, x))
