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
    for food in stock:
        for item in fresh:
            start, end = map(int, item.split('-'))
            if int(food) >= start and int(food) <= end:
                if food not in fresh_stock:
                    fresh_stock.append(food)

    return fresh_stock

print(len(check_food(fresh, stock)))
    







