def generate(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['0', '1']
    else:
        L = []
        for i in generate(n - 1):
            L.append('0' + i)
        for i in generate(n - 1):
            L.append('1' + i)
        return L

print(generate(40))
