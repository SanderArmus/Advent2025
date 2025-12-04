from pathlib import Path


data = [
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
    [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8],
    [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1],
]

def load_matrix():
    data_file = Path(__file__).resolve().parent / 'adv03.txt'
    rows = []
    with data_file.open('r') as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                rows.append(list(stripped))
    return rows

data = load_matrix()



def get_two(data):
    biggest=[]
    for line in data:
        first_number=str(max(line[:-1]))
        firstindex = line.index(max(line[:-1]))
        second_number = str(max(line[firstindex+1:]))

        biggest.append(int(first_number+second_number))
    return biggest
        

print(get_two(data))

print(sum(get_two(data)))