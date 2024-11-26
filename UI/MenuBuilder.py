from UI.MenuItem import MenuItem

class MenuBuilder:
    def __init__(self, menu: list[MenuItem]):
        self.Menu = menu

    def initialize(self):
        try:
            print("Please choose: \n")
            for item in self.Menu:
                print(item.key, item.description)
            choice = input("> ")
            item = self.get_menu_item(choice)
            item.func(*item.args)
        except ValueError:
            print("No such item in menu.")

    def get_menu_item(self, key: str) -> MenuItem:
        for item in self.Menu:
            if item.key == key:
                return item
        raise ValueError()

    def add_menu_item(self, item: MenuItem):
        self.Menu = self.Menu.append(item)