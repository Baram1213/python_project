text = input().split()

count = 0
for word in text:
    word = word.strip(',.')    
    if word == 'the':
        count += 1

print(count)
