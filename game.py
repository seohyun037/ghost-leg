from matplotlib import pyplot as plt
import random

start = int(input("어디서 시작할지 숫자로 입력"))
a = [1,2,3,4,5,6,7]
b = [0,0,0,0,0,0,0]

for _ in range(1000):
    ladder = 0
    player = start - 1
    board = []
    for i in range(20):
        board.append(['│', '│', '│', '│', '│', '│', '│']) # 7명, 20개의 세로 사다리


    while ladder < 15: # 가로 사다리 15개 배치
        x = random.randint(0, 19)
        y = random.randint(0,5)
        if board[x][y] == '─' or board[x][y + 1] == '─':
            continue
        board[x][y] = '─'
        board[x][y + 1] = '─'
        ladder += 1

    for i in range(20):
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