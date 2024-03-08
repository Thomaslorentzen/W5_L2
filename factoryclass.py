from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name, price, quantity_available=0):
        self.id = Item._generate_id()  # Call the class method directly
        self.name = name
        self.price = price
        self.quantity_available = quantity_available
    
    @classmethod
    def _generate_id(cls):
        # Use a global counter to keep track of the highest ID assigned
        global _highest_id
        item_id = _highest_id
        _highest_id += 1
        return item_id
    
    @abstractmethod
    def display(self):
        pass
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
    
    def get_quantity_available(self):
        return self.quantity_available
    
    def pick_item(self, quantity=1):
        if quantity > self.quantity_available:
            raise ValueError("Not enough available for your order")
        self.quantity_available -= quantity
        return f"Picked {quantity} {self.name}(s)"

class GuitarItem(Item):
    def display(self):
        print(f"ID: {self.id}, name: {self.name}, price: {self.price}")

class AmplifierItem(Item):
    def display(self):
        print(f"ID: {self.id}, name: {self.name}, price: {self.price}")

class PedalItem(Item):
    def display(self):
        print(f"ID: {self.id}, name: {self.name}, price: {self.price}")

class AccessoryItem(Item):
    def display(self):
        print(f"ID: {self.id}, name: {self.name}, price: {self.price}")

class ItemFactory:
    @staticmethod
    def create_item(item_type, name, price, quantity_available=0):
        if item_type == "guitar":
            return GuitarItem(name, price, quantity_available)
        elif item_type == "amplifier":
            return AmplifierItem(name, price, quantity_available)
        elif item_type == "pedal":
            return PedalItem(name, price, quantity_available)
        elif item_type == "accessory":
            return AccessoryItem(name, price, quantity_available)
        else:
            raise ValueError("Invalid item type")

# Initialize the global counter
_highest_id = 1


