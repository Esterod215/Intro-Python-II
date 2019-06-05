# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name,currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    
    def checkMovement(self,directionNumber,currentRoom):
    
        if currentRoom == "Outside Cave Entrance":
        
            if not directionNumber == 1:
                return False
        
            else:
                self.currentRoom = "foyer"
                return True
    
        elif currentRoom == "Foyer":
        
            if self.directionNumber == 1:
                currentRoom = "overlook"
                return True
        
            elif directionNumber == 2:
                currentRoom = "narrow"
                return True
        
            elif directionNumber == 4:
                currentRoom = "outside"
                return True
        
            else:
                return False
    
        else:
            print("logic failed")
            return False
        
