from factoryclass import AmplifierItem, GuitarItem, Item, ItemFactory
import unittest

class FactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = ItemFactory()
        self.guitar = self.factory.create_item("guitar", "Guitar", 100)
        self.amplifier = self.factory.create_item("amplifier", "Amplifier", 200)
        self.pedal = self.factory.create_item("pedal", "Pedal", 300)
        self.accessory = self.factory.create_item("accessory", "Accessory", 400)
    
    def test_create_guitar(self):
        self.assertEqual(self.guitar.name, "Guitar")
        self.assertEqual(self.guitar.price, 100)

    def test_create_amplifier(self):
        self.assertEqual(self.amplifier.name, "Amplifier")
        self.assertEqual(self.amplifier.price, 200)
    
    def test_create_pedal(self):
        self.assertEqual(self.pedal.name, "Pedal")
        self.assertEqual(self.pedal.price, 300)
    
    def test_create_accessory(self):
        self.assertEqual(self.accessory.name, "Accessory")
        self.assertEqual(self.accessory.price, 400)
    
    def test_create_item(self):
        item = self.factory.create_item("guitar", "Guitar", 100)
        self.assertEqual(item.name, "Guitar")
        self.assertEqual(item.price, 100)
    
    def test_item_id_generation(self):
        # Ensure _id_counter is initially 1
        self.assertEqual(Item._id_counter, 1)

        # Create instances and verify IDs
        guitar1 = GuitarItem("Guitar", 100)
        self.assertEqual(guitar1.get_id(), 1)

        guitar2 = GuitarItem("Guitar", 100)
        self.assertEqual(guitar2.get_id(), 2)

        # Ensure _id_counter has been incremented
        self.assertEqual(Item._id_counter, 3)


if __name__ == "__main__":
    unittest.main()