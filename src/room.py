# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name , description, items):
        self.name = name
        self.description = description
        self.items = items
    def __str__(self):
        return (f"location: {self.name}. A sign reads {self.description}")