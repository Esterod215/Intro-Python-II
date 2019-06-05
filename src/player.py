# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name,currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    
    def checkMovement(self,directionNumber,currentRoom):
    
        if self.currentRoom == "Outside Cave Entrance":
        
            if not self.directionNumber == 1:
                return False
        
            else:
                self.currentRoom = "foyer"
                return True
    
        elif self.currentRoom == "Foyer":
        
            if self.directionNumber == 1:
                self.currentRoom = "overlook"
                return True
        
            elif self.directionNumber == 2:
                self.currentRoom = "narrow"
                return True
        
            elif self.directionNumber == 4:
                self.currentRoom = "outside"
                return True
        
            else:
                return False
    
        else:
            print("logic failed")
            return False
        
