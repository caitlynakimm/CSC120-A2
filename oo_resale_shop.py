from computer import *
from typing import Optional # for the optional parameter new_os in refurbish method

# should keep track of store's inventory (list of individual computer instances, buying/selling/updating prices/refurbishing computers)
class ResaleShop:

    # What attributes will it need?
    # where list of computers and their details are stored
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?

    # adds a new computer to inventory
    def buy(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        new_computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.append(new_computer)

    # updates price of a particular computer
    def update_price(self, item_id: int, new_price: int):
        if 0 <= item_id < len(self.inventory): #starting item index at 0, so item index must be less than # of computers in inventory 
            self.inventory[item_id].update_price(new_price) # updates the price of a computer at a particular index in inventory
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
    # removes a particlar computer in inventory
    def sell(self, item_id: int):
        if 0 <= item_id < len(self.inventory): #starting item index at 0, so item index must be less than # of computers in inventory
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # prints all computer details in inventory
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.description}, {item.processor_type}, {item.hard_drive_capacity}, {item.memory}, {item.operating_system}, {item.year_made}, {item.price}')
        else:
            print("No inventory to display.")
    
    # updates a particular computer's selling price and new operating system (if given)
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if 0 <= item_id < len(self.inventory): # starting item index at 0, so item index must be less than # of computers in inventory
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.update_price(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
