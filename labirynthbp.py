
# Game map blueprint
map = {
    "start": {
        "description": "You are in a dark corridor. You can go north or east. [NSWE]",
        "N": "hall",
        "E": "tunnel"
    },
    "hall": {
        "description": "A large echoing hall. You can go back south.",
        "S": "start"
    },
    "tunnel": {
        "description": "A narrow tunnel leading nowhere. You can go back west.",
        "W": "start"
    }
}

position = "start"

while True:
    print("\n" + map[position]["description"])
    move = input("> ").upper()

    if move in map[position]:
        position = map[position][move]
    else:
        print("You can't go that way!")