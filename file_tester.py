name = 'Sakshi'
score = '60'
change = False
file = open('scores.txt')
for line in file.readlines():
    line = str(line).strip()
    print(line)
    if line[0: 2] == 'NN':
        print(line[3:])
        if int(line[3:]) < int(score):
            change = True
print(change)
file.close()
if change:
    file = open('scores.txt', 'w')
    file.write(f'SS {name}\nNN {score}')
    file.close()
