fresh = ['3-5', '10-14', '16-20', '12-18']
stock = ['1', '5', '8', '11', '17', '32']

def getdata():
    fresh = []
    stock = []

    with open("adv05.txt", "r") as f:
        lines = f.read().splitlines()

    separator_found = False

    for line in lines:
        if line.strip() == "":
            separator_found = True
            continue

        if not separator_found:
            fresh.append(line)
        else:
            stock.append(line)

    return fresh, stock

fresh, stock = getdata()

def check_food(fresh,stock):
    fresh_stock=[]
    for item in fresh:
        start, end = map(int, item.split('-'))
        fresh_stock.append((start,end))
        
    fresh_stock.sort()
    merged = []
    cur_start, cur_end = fresh_stock[0]
    
    for start , end in fresh_stock[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start,end
    merged.append((cur_start, cur_end))
    total = 0
    for start, end in merged:
        total += (end - start +1)
    return total

print(check_food(fresh, stock))
    







