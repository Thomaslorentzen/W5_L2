import io
import sys
import unittest
from InventoryClass import Inventory, InventoryManagement, InventoryObserver

class TestInventoryManagement(unittest.TestCase):
    def test_singleton_instance(self):
        # Test whether InventoryManagement is implemented as a singleton
        inventory1 = InventoryManagement()
        inventory2 = InventoryManagement()
        self.assertIs(inventory1, inventory2)

    def test_update_inventory(self):
        # Test updating inventory
        inventory = InventoryManagement()
        inventory.update_inventory("apple", 10)
        self.assertEqual(inventory.get_inventory()["apple"], 10)

        inventory.update_inventory("banana", 5)
        self.assertEqual(inventory.get_inventory()["banana"], 5)

        inventory.update_inventory("apple", 5)
        self.assertEqual(inventory.get_inventory()["apple"], 15)

  

    def test_detach_observer(self):
        # Test detaching observer
        inventory = Inventory()
        observer = InventoryObserver(inventory)
        inventory.attach(observer)
        
        inventory.update_inventory("apple", 10)
        self.assertEqual(inventory._inventory["apple"], 10)

        # Detach observer
        inventory.detach(observer)
        inventory.update_inventory("banana", 5)

        # Observer should not receive the update
        captured_output = io.StringIO()
        sys.stdout = captured_output
        inventory.notify()
        sys.stdout = sys.__stdout__
        self.assertNotIn("Updated inventory: {'banana': 5}", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
