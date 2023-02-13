class Door:
    def __init__(self):
        self.is_opened = False

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

class BlockedDoor(Door):

    def open_door(self):
        raise AttributeError("The BlockedDoor cannot be opened")

    def close_door(self):
        raise AttributeError("The BlockedDoor cannot be closed")


blocked_door = BlockedDoor()
print(blocked_door.is_opened)
blocked_door.open_door() # Stop the program
print(blocked_door.is_opened)
