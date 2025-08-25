print("ShashankGowdaL 1BM23CS311")

rooms = {'A': True, 'B': True}

current_room = input("Enter starting room (A/B): ").upper()
while current_room not in rooms:
    current_room = input("Invalid input. Enter starting room (A/B): ").upper()

def suck(room):
    if rooms[room]:
        print(f"Sucking dirt in room {room}.")
        rooms[room] = False
    else:
        print(f"Room {room} is already clean.")

def move(direction):
    global current_room
    if direction == "left" and current_room == "B":
        current_room = "A"
        print("Moved left to room A.")
    elif direction == "right" and current_room == "A":
        current_room = "B"
        print("Moved right to room B.")
    else:
        print("Cannot move in that direction from current room.")

while rooms['A'] or rooms['B']:
    print(f"\nCurrent room: {current_room}")
    print(f"Room A dirty? {rooms['A']}")
    print(f"Room B dirty? {rooms['B']}")
    action = input("Enter action (left, right, suck): ").lower()
    if action == "suck":
        suck(current_room)
    elif action in ["left", "right"]:
        move(action)
    else:
        print("Invalid action. Try again.")

print("Both rooms are clean.")
