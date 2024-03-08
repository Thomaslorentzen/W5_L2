import io
import sys
import unittest
from CommandClass import salesTransactionsCommand, restockCommand

class testCommand(unittest.TestCase):
    def setUp(self):
            # Initialize inventory for testing
            self.inventory = {'guitar': 10, 'amp': 5, 'pedal': 3, 'accessory': 20}

    def test_salesTransactionsCommand_execute(self):
            # Test salesTransactionsCommand
            command = salesTransactionsCommand(self.inventory, 'guitar', 2)
            command.execute()
            self.assertEqual(self.inventory['guitar'], 8)  # Check inventory after sales transaction

            # Test for item not in inventory
            command = salesTransactionsCommand(self.inventory, 'drum', 1)
            captured_output = io.StringIO()
            sys.stdout = captured_output
            command.execute()
            sys.stdout = sys.__stdout__
            self.assertIn("Item not in inventory", captured_output.getvalue())  # Check for printed message

    def test_restockCommand_execute(self):
            # Test restockCommand
            command = restockCommand(self.inventory, 'amp', 3)
            command.execute()
            self.assertEqual(self.inventory['amp'], 8)  # Check inventory after restocking

            # Test for new item restocking
            command = restockCommand(self.inventory, 'cable', 5)
            command.execute()
            self.assertEqual(self.inventory['cable'], 5)  # Check inventory for newly restocked item

if __name__ == '__main__':
    unittest.main()