from matplotlib import pyplot as plt
import random

start = int(input("어디서 시작할지 숫자로 입력: "))

"""people: 사람 인원수
bridge: 가로 사다리 수
rail(= bridge * 2): 세로 사다리 수"""

people = 7
bridge = 10 # 가로
rail = bridge * 2 # 세로

a = []
b = []
line = []

for i in range(people):
    a.append(i+1)
    b.append(0)
    line.append('│')

for _ in range(10000): # 10000번 반복
    ladder = 0
    player = start - 1
    board = []
    for i in range(rail):
        board.append(line.copy())


    while ladder < bridge: 
        x = random.randint(0, rail - 1)
        y = random.randint(0, people - 2)
        if board[x][y] == '─' or board[x][y + 1] == '─':
            continue
        board[x][y] = '─'
        board[x][y + 1] = '─'
        ladder += 1

    for i in range(rail):
        cnt = 0
        if board[i][player] == '─':
            for j in range(player):
                if board[i][j] == '─':
                    cnt += 1
            if cnt % 2 == 0:
                player += 1
            else:
                player -= 1
        else:
            continue

    b[player] += 1

plt.bar(a, b)
plt.show()