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


#number = "121212121212"


def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors



def get_chunks(number):
    s = str(number)
    divisors = get_divisors(len(s))
    all_chunks = []
    for n in divisors:
        chunks = []
        i = 0
        while i < len(s):
            chunk = s[i:i+n]
            chunks.append(int(chunk))
            i += n
        all_chunks.append(chunks)
    return all_chunks



def check_chunks(number):
    all_chunks = get_chunks(number)
    for chunk_list in all_chunks:
        if len(chunk_list) > 1 and chunk_list.count(chunk_list[0]) == len(chunk_list):
            return True
    return False

        

def get_all_invalids(data):
    all_invalids = []
    for item in data:
        start, end = map(int, item.split('-'))
        number = start
        while number <= end:
            print(number)
            if check_chunks(number):
                all_invalids.append(number)
            number+=1
    print(all_invalids)
    return all_invalids

print(sum(get_all_invalids(data)))
            
        




''' def find_invalid(data):
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
 '''

