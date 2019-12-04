import reader


def add_item(db):
    pid = input("Product ID: ")
    name = input("Name: ")
    price = int(input("Price: "))
    count = int(input("Count: "))

    count = count if pid not in db else count + db[pid]["count"]

    db[pid] = {"name": name, "price": price, "count": count}


def search_item(db):
    b = input("Please, enter item name (or part of it): ")
    result = {}
    count = 0
    for a in db:
        c = db[a]['name']
        if b in db[a]['name']:
            count += 1
            result[a] = db[a]

    if not count:
        print("No items found:")
        exit()
        print('doesnt it')

    print(f"Found {count} items:")
    for item in result:
        reader.print_item(item, result)


def reg_sale(db):
    print('Please, enter item code and sale count:')

    cde = input('Code: ')
    while not cde in db:
        print("There is not enough of item in store")
        cde = input('Code: ')

    cnt = int(input('Count: '))

    db[cde] = {"name": db[cde]["name"], "price": db[cde]["price"],
               "count": 0 if db[cde]["count"] <= cnt else db[cde]["count"] - cnt}
    print("Your sale is registered successfully!")


def x_exit(db):
    db.close()
    exit()
