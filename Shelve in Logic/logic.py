import shelve
import menu

db = shelve.open("items.db")

menu.menu(db)

