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
def number_adj (data):
    rolls = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            rollcount = 0
            if data[i][j]=='@':
                if i + 1 < len(data) and data[i+1][j]=='@':
                    rollcount += 1
                if j + 1 < len(data[i]) and data[i][j+1]=='@':
                    rollcount += 1    
                if i - 1 >= 0 and data[i-1][j]=='@':
                    rollcount += 1
                if j - 1 >= 0 and data[i][j-1]=='@':
                    rollcount += 1
                if i + 1 < len(data) and j + 1 < len(data[i]) and data[i+1][j+1]=='@':
                    rollcount += 1
                if i - 1 >= 0 and j - 1 >= 0 and data[i-1][j-1]=='@':
                    rollcount += 1
                if i + 1 < len(data) and j - 1 >= 0 and data[i+1][j-1]=='@':
                    rollcount += 1   
                if i - 1 >= 0 and j + 1 < len(data[i]) and data[i-1][j+1]=='@':
                    rollcount += 1     
                if rollcount < 4:
                    rolls += 1
    return rolls 
print(number_adj(data))
