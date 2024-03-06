from DBConnect import DatabaseConnection
from factoryclass import ItemFactory
from CommandClass import Command, salesTransactionsCommand
from InventoryClass import Inventory, InventoryManagement, InventoryObserver

def main():
    print("Starting main function...")  # Check if main function is being executed
    # Establish database connection
    db_connection = DatabaseConnection.connection("example.db")

    inventory = Inventory()    
    # Create items
    factory = ItemFactory()
    observer = InventoryObserver(inventory)
    inventory.attach(factory)

    inventory_manager = InventoryManagement()
    

    guitar_item1 = factory.create_item("guitar", "Fender Stratocaster Sunburst", 900)
    guitar_item2 = factory.create_item("guitar", "Yamaha 2540 Acoustic Steel", 500)

    amp_item1 = factory.create_item("amplifier", "Marshall", 270)

    pedal_item1 = factory.create_item("pedal", "SD-1 distortion", 400)

    accessory_item1 = factory.create_item("accessory", "Nanoweb strings 53-12", 40)
    accessory_item2 = factory.create_item("accessory","Gear4Music picks, 48pc.", 15)
    
    # Display items
    print("Displaying items:")
    guitar_item1.display()
    guitar_item2.display()
    amp_item1.display()
    pedal_item1.display()
    accessory_item1.display()
    accessory_item2.display()
    

    #Test updates of inventory
    inventory_manager.update_inventory("Fender Stratocaster Sunburst", 10)
    inventory_manager.update_inventory("Yamaha 2540 Acoustic Steel", 7)
    inventory_manager.update_inventory("Marshall", 5)
    inventory_manager.update_inventory("Gear4Music picks, 48pc.", 2)
    
    #Let us make the transaction commands:
    sales_transaction_command = salesTransactionsCommand(inventory_manager.get_inventory(), "Fender Stratocaster Sunburst", 7)

    sales_transaction_command.execute()

    #Let us have a look at the updated inventory
    print("Updated inventory")
    for item, quantity in inventory_manager.get_inventory().items():
        print(f"{item}: {quantity}")



    # Close database connection
    db_connection.close()

if __name__ == "__main__":
    main()



