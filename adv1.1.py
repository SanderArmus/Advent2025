from pathlib import Path

#data = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

def getdata():
    data_file = Path(__file__).resolve().parent / 'adv01.txt'
    with data_file.open("r") as file:
        data = file.read().splitlines()
    return data

data = getdata()

def getpassword(data):
    password = 0
    position = 50
    for i in data:
        symbol = i[0]
        if symbol == 'L':
            position = position - int(i[1:])
            while position < 0:
                position = position + 100
        elif symbol == 'R':
            position = position + int(i[1:])
            while position >= 100:
                position = position - 100
        #print(position)
        if position == 0:
            password = password + 1
    return password


print(getpassword(data))
