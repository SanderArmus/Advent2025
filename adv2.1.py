from pathlib import Path

data = ['11-22', '95-115', '998-1012', '1188511880-1188511890', '222220-222224',
        '1698522-1698528', '446443-446449', '38593856-38593862', '565653-565659',
        '824824821-824824827', '2121212118-2121212124']

def get_data():
    data_file = Path(__file__).resolve().parent / 'adv02.txt'
    with data_file.open('r') as f:
        line = f.read().strip() 
    data = line.split(',') 
    return data

data = get_data()

def find_invalid(data):
    invalids = []
    for item in data:
        start, end = map(int, item.split('-'))
        num = start
        while num <= end:
            s = str(num)
            if len(s) % 2 == 0:
                half = len(s) // 2
                if s[:half] == s[half:]:
                    invalids.append(num)
            num += 1
    return invalids

print(sum(find_invalid(data)))


