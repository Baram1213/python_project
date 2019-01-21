with open('words.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        if line == line[::-1]:
            print(line)
