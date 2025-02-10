from computer import *
class ResaleShop:

    # What attributes will it need?
    # should keep track of store's inventory (list of individual computer instances, buying a computer (adding to inventory), selling a computer (removing from inventory))
    inventory = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = inventory

    # What methods will you need?
    def buy(self, computer):
        #1. call Computer(...) constructor
        #   to create a new Computer instance
        self.inventory.append(computer)
        #2. call inventory.append(...) to add the
        #   new Computer instance to the inventory  
        return self.inventory.index(computer)

    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")
    
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
