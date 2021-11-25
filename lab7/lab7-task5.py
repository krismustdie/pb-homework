def cifr(s, a, counter):
    if s[a] == '.':
        print(f'ans: {counter}')
    else:
        try:
            int(s[a])
            cifr(s, a + 1, counter + 1)
        except ValueError:
            cifr(s, a + 1, counter)


with open('input.txt') as f:
    cifr(f.read(), 0, 0)
