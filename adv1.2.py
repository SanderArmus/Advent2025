from pathlib import Path

data = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

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
        dir = i[0]
        steps = int(i[1:])
        
        for step in range(steps):
            if dir == 'R':
                position = (position + 1) % 100
            else:
                position = (position - 1) % 100
            
            if position == 0:
                password += 1
    
    return password



print(getpassword(data))
