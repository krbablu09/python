def start_game():
    print("🌴 Welcome to Jungle Escape Adventure!")
    print("You are lost in a jungle.")
    print("Choose a direction: left or right?")

    choice1 = input(">> ").lower() 

    if choice1 == "left":
        river_scene()

    elif choice1 == "right":
        cave_scene()

    else:
        print("Invalid choice! Game Over.")

def river_scene():
    print("\n🌊 You reached a river.")
    print("Do you swim or build a raft?")

    choice2 = input(">>").lower()

    if choice2 == "swim":
        print("🐊 Crocodile attacked you! Game Over.")

    elif choice2 == "raft":
        treasure_scene()

    else:
        print("Invalid choice! Game Over.")

def cave_scene():
    print("\n🕳️ You entered a dark cave.")
    print("You see a sleeping bear.")
    print("Do you sneak or attack?")

    choice3 = (">> ").lower()

    if choice3 == "sneak":
        treasure_scene()

    elif choice3 == "attack":
        print("🐻 Bear woke up! Game Over.")    

    else:
        print("Invalid choice! Game Over.")

def treasure_scene():
    print("\n💎 You found a treasure chest!")  
    print("Do you open it or leave it?")

    choice4 = input(">> ").lower()

    if choice4 == "open it":
        print("🎉 Congratulations! You Win") 

    elif choice4 == "leave it":
        print("You safely leave the jungal. You Survived!")

    else:
        print("Invalid choice! Game Over.")             

start_game()