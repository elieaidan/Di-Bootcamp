class Door:
    def __init__(self, is_opened):
        self.is_opened = True
    
    def oper_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False    

class BlockDoor(Door):

    def oper_door(self):
        print("Error")        

    def close_door():
        print("Error")
