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



def getmax(data):
    biggest=[]
    for line in data:
        n=12
        lastindex=0
        linebiggest=[]
        while n > 0:
            maximum = max(line[:len(line)-n+1])
            maxindex=line.index(maximum)
            linebiggest.append(maximum)
            line=line[maxindex +1:]
            n-=1
        biggest.append(linebiggest)
    return biggest
        

print(getmax(data))

def get_powers(data):
    numbers=getmax(data)
    powers=[]
    for number in numbers:
        power=" "
        for element in number:
            power+=str(element)
        powers.append(power)
    return powers

print(get_powers(data))


def getsum(data):
    powers = get_powers(data)
    totalpower = 0
    for power in powers:
        totalpower +=int(power)
    return totalpower

print(getsum(data))


