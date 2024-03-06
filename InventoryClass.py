class Inventory:
    def __init__(self):
        self._observers = []
        self._inventory = {}

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def update_inventory(self, item, quantity):
        self._inventory[item] = quantity
        self.notify()


class InventoryObserver:
    def __init__(self, inventory):
        self._inventory = inventory
    
    def update(self):
        print("Updated inventory: " + str(self._inventory))    


class InventoryManagement:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inventory = {}
        return cls._instance
    
    def get_inventory(self):
        return self._instance._inventory
    
    def update_inventory(self, item, quantity):
        if item in self._instance._inventory:
            self._instance._inventory[item] += quantity
        else:
            self._instance._inventory[item] = quantity

