import service
import reader
import shelve

db = shelve.open("items.db")

def menu():

    print('Available actions:')
    print('a - Add or update an item')
    print('f - Search for an item')
    print('s - Register a sale')
    print('p - Show Menu')
    print('x - Exit')
    print('Enter command code', end=' ')
    cmd = input().lower()
    if cmd in COMMANDS:
        COMMANDS[cmd](db)
        menu()
    print('Wrong Command!\n')
    menu()




COMMANDS = {'a': service.add_item,
            'f': service.search_item,
            's': service.reg_sale,
            'p': reader.print_table,
            'x': service.x_exit,
            }



