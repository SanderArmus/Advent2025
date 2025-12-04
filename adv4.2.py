from pathlib import Path

data = [
    ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
    ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
    ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
    ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
    ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
    ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
    ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
    ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
    ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
    ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.'],
]

def load_matrix():
    data_file = Path(__file__).resolve().parent / 'adv04.txt'
    rows = []
    with data_file.open('r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                rows.append(list(stripped))
    return rows

data = load_matrix()


def number_adj(data):
    rolls = 0
    removed_rolls = 1

    while removed_rolls > 0:
        removed_rolls = 0
        to_remove = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != '@':
                    continue
                rollcount = 0
                if i + 1 < len(data) and data[i+1][j] == '@':
                    rollcount += 1
                if j + 1 < len(data[i]) and data[i][j+1] == '@':
                    rollcount += 1
                if i - 1 >= 0 and data[i-1][j] == '@':
                    rollcount += 1
                if j - 1 >= 0 and data[i][j-1] == '@':
                    rollcount += 1
                if i + 1 < len(data) and j + 1 < len(data[i]) and data[i+1][j+1] == '@':
                    rollcount += 1
                if i - 1 >= 0 and j - 1 >= 0 and data[i-1][j-1] == '@':
                    rollcount += 1
                if i + 1 < len(data) and j - 1 >= 0 and data[i+1][j-1] == '@':
                    rollcount += 1
                if i - 1 >= 0 and j + 1 < len(data[i]) and data[i-1][j+1] == '@':
                    rollcount += 1
                if rollcount < 4:
                    to_remove.append((i, j))

        for (i, j) in to_remove:
            data[i][j] = '.'

        removed_rolls = len(to_remove)
        rolls += removed_rolls

    return rolls

print(number_adj(data))
