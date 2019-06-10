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
        
            if directionNumber == 1:
                self.currentRoom = "overlook"
                return True
        
            elif directionNumber == 2:
                self.currentRoom = "narrow"
                return True
        
            elif directionNumber == 4:
                self.currentRoom = "outside"
                return True
        
            else:
                return False
        
        elif currentRoom == "Grand Overlook":
            if not directionNumber == 4:
                return False
            else:
                self.currentRoom = "foyer"
                return True

        elif currentRoom == "Narrow Passage":
            if directionNumber == 1:
                self.currentRoom = "treasure"
                return True
            
            elif directionNumber == 3:
                self.currentRoom = "foyer"
                return True
                
            else:
                return False

        elif currentRoom == "Treasure Chamber":
            if not directionNumber == 4:
                return False
            else:
                self.currentRoom = "narrow"

    
        else:
            return False
        
