from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class salesTransactionsCommand(Command):
    def __init__(self, inventory, item, quantity):
        self.inventory = inventory
        self.item = item
        self.quantity = quantity
    
    def execute(self):
        if self.item in self.inventory:
            self.inventory[self.item] -= self.quantity
        else:
            print("Item not in inventory")
    
class restockCommand(Command):
    def __init__(self, inventory, item, quantity):
        self.inventory = inventory
        self.item = item
        self.quantity = quantity

    def execute(self):
        if self.item in self.inventory:
            self.inventory[self.item] += self.quantity
        else:
            self.inventory[self.item] = self.quantity
