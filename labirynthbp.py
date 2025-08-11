map = {
    "start": {
        "description": "You are in a dark corridor. You can go north or east. [NWSE]",
        "N": "hall",
        "E": "tunnel"
    },
    "hall": {
        "description": "A large echoing hall. You can go back south, east or north.",
        "E": "ltunnel",
        "N": "room",
        "S": "start"
    },
    "room":{
         "description": "A small, empty room, what a waste of time, go back south",
         "S": "hall"
    },
    "ltunnel":{
        "description": "A long uncanny tunnel with a bright light at the end, you can go back west or continue east",
        "E": "Exit",
        "W": "hall"
    },
    "Exit":{
        "description": "Congratulations! You found the exit! You can go back west to explore the maze, but dont get lost!",
        "W": "ltunnel"
    },
    "tunnel": {
        "description": "A narrow tunnel leading to a strange door. You can go back west or continue east.",
        "W": "start",
        "E": "snake"
    },
    "snake": {
         "description": " A room filled with venomous snakes, before you could react they lunge at you and kill you.",
},
}

position = "start"

while True:
    print("\n" + map[position]["description"])
    move = input("> ").upper()

    if move in map[position]:
        position = map[position][move]
    else:
        print("You can't go that way!")
