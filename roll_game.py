import random
from colorama import Fore, Style, init

init()

prizes = {
    2: "MONEY",
    12: "CAR",
    18: "HOME",
    99: "something... questionable",
    8: "$100",
    49: "$$$ 100,000,000 $$$",
    38: "BOOK",
    82: "FREE TICKET",
    52: "FREE TICKET",
    74: "FREE TICKET",
    11: "FREE TICKET",
    1: "FREE TICKET",
    45: "FREE TICKET",
    17: "FREE TICKET",
    95: "FREE TICKET",
    96: "$45",
    67: "$10",
    76: "$10",
    88: "$10",
    50: "$100",
    91: "$50",
    56: "$50",
    39: "$200",
    34: "$5000",
    51: "$2000"
}

colors = [Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN]

start = input("Type START to play: ")

if start.lower() == "start":
    number = random.randint(1, 100)
    print(f"Your number is {number}")

    if number in prizes:
        chosen_color = random.choice(colors)
        print(chosen_color + f"You won {prizes[number]}!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "No prize... try again 😐" + Style.RESET_ALL)
else:
    print("Game not started.")


