# creates the attributes and method for each computer
class Computer:

    # What attributes will it need?
    # saves these details for each computer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    # creates a computer object with the attributes from above
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
    # What methods will you need?
    
    # updates a computer's price
    def update_price(self, new_price: int):
        self.price = new_price

